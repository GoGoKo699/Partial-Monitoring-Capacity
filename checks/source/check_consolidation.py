#!/usr/bin/env python3
"""Four checks of the consolidated proof's explicit intermediate claims.

Usage: python check_consolidation.py --output NEW.json
Uses byte-preserved helpers from prior/check_audit.py, never updates a reference.
The capacity theorem is analytical; these are finite identity/scope checks.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import math
from pathlib import Path
import unittest
import numpy as np
from scipy.optimize import brentq, minimize_scalar

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('audit_helpers', ROOT/'prior/check_audit.py')
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
REPORT = {}


def frame(d, outcomes, rng):
    z = rng.normal(size=(outcomes,d))+1j*rng.normal(size=(outcomes,d))
    q,_ = np.linalg.qr(z)
    return q


def rate_qubit(a,b,q):
    return min(u.h2(a*q),u.h2((1-b)*q))-u.h2(b*q)


def left_derivative(a,b,q):
    def term(x):
        return 0. if x == 0 else x*math.log2((1-x*q)/(x*q))
    return term(a)-term(b)


def qubit_optimum(a,b):
    if a <= b:return 0.,0.,'zero'
    kink = 1/(1+a-b)
    if left_derivative(a,b,kink) >= -1e-14:
        q=kink;mode='entropy-crossover'
    else:
        q=brentq(lambda z:left_derivative(a,b,z),1e-14,kink,xtol=3e-15)
        mode='stationary-left-cut'
    return q,rate_qubit(a,b,q),mode


class Checks(unittest.TestCase):
    def test_actual_flagged_channel_and_complement_degrade(self):
        rng=np.random.default_rng(710061);rows=[]
        for a,b,c in [(.2,.08,.72),(.6,.3,.1),(.3,.3,.4),(.2,0.,.8)]:
            v=u.splitter(a,b,c,1).reshape(2,2,2,2)
            meas=frame(2,6,rng);m=len(meas)
            # B,X are sent; E,Y are a true complementary output. X and Y copy x.
            j=np.zeros((2,m,2,m,2),complex)
            for x,row in enumerate(meas):j[:,x,:,x,:]=np.einsum('bedi,d->bei',v,row)
            j=j.reshape(4*m*m,2)
            self.assertLess(np.linalg.norm(j.conj().T@j-np.eye(2)),3e-14)
            rho=u.random_rho(2,rng);allout=j@rho@j.conj().T
            out=u.ptrace(allout,[2,m,2,m],[0,1]);comp=u.ptrace(allout,[2,m,2,m],[2,3])
            sim=sum(np.kron(k,np.eye(m))@out@np.kron(k,np.eye(m)).conj().T for k in u.loss_kraus(b/a,2))
            self.assertLess(np.linalg.norm(sim-comp),3e-14)
            _,branches=u.helper_branches(v.reshape(8,2),rho,meas,2)
            difference=u.entropy(out)-u.entropy(comp)
            conditional=sum(p*(u.entropy(B)-u.entropy(E))for p,B,E in branches)
            self.assertAlmostEqual(difference,conditional,places=12)
            rows.append(dict(weights=[a,b,c],outcomes=m,stinespring_dimension=len(j),
                complementary_simulation_error=float(np.linalg.norm(sim-comp)),coherent_information=difference))
        REPORT['refined_helper_channel']={'checks':rows,'scope':'A genuine flagged complement includes a copy of the classical outcome; arbitrary rank-one POVMs remain degradable.'}

    def test_discarded_encoder_ancilla_does_not_raise_the_converse(self):
        rng=np.random.default_rng(710062);rows=[]
        for a,b,c in [(.2,.08,.72),(.6,.3,.1),(.3,.3,.4),(.2,0.,.8)]:
            V=u.splitter(a,b,c,1).reshape(2,2,2,2)
            meas=frame(2,4,rng)
            for trial in range(3):
                psi=rng.normal(size=(2,2,2))+1j*rng.normal(size=(2,2,2));psi/=np.linalg.norm(psi)
                total=np.einsum('rfi,bedi->rfbed',psi,V)
                ic_input=0.;ic_message=0.;conditional_ancilla=0.
                for row in meas:
                    x=np.einsum('rfbed,d->rfbe',total,row).reshape(-1)
                    p=float(np.vdot(x,x).real)
                    state=np.outer(x,x.conj())/p
                    B=u.ptrace(state,[2]*4,[2]);E=u.ptrace(state,[2]*4,[3]);FE=u.ptrace(state,[2]*4,[1,3])
                    ic_input+=p*(u.entropy(B)-u.entropy(E))
                    ic_message+=p*(u.entropy(B)-u.entropy(FE))
                    conditional_ancilla+=p*(u.entropy(FE)-u.entropy(E))
                self.assertGreaterEqual(conditional_ancilla,-4e-13)
                self.assertAlmostEqual(ic_input-ic_message,conditional_ancilla,places=12)
                self.assertLessEqual(ic_message,ic_input+4e-13)
                rows.append(dict(weights=[a,b,c],trial=trial,purified_input_coherent_information=ic_input,
                    actual_message_coherent_information=ic_message,ancilla_conditional_entropy=conditional_ancilla))
        # Scope: without degradability, this comparison can fail.
        a,b,c=.1,.7,.2;rho=np.eye(2)/2
        _,branches=u.helper_branches(u.splitter(a,b,c,1),rho,np.eye(2),2)
        negative=sum(p*(u.entropy(B)-u.entropy(E))for p,B,E in branches)
        self.assertLess(negative,-.1)
        REPORT['general_encoder_check']={'records':rows,'antidegradable_scope_control':negative,
            'scope':'Tests the weak-monotonicity proof for a discarded encoding ancilla F. It does not simulate coding or assume all encoders are isometries.'}

    def test_rate_gap_decomposes_without_omitting_a_hidden_environment(self):
        rng=np.random.default_rng(710063);rows=[]
        for a,b,c in [(.2,.08,.72),(.6,.2,.2),(.2,0.,.8)]:
            cut=4;d=cut+1;V=u.splitter(a,b,c,cut);rho=u.random_rho(d,rng)
            mean=float(np.dot(np.arange(d),np.diag(rho).real));budget=mean+.7
            for name,meas in [('count',np.eye(d)),('fourier',np.fft.fft(np.eye(d))/math.sqrt(d)),('overcomplete',frame(d,2*d,rng))]:
                full,branches=u.helper_branches(V,rho,meas,d)
                B=u.ptrace(full,[d]*3,[0]);E=u.ptrace(full,[d]*3,[1])
                sb,se=u.entropy(B),u.entropy(E)
                cb=sum(p*u.entropy(bb)for p,bb,ee in branches);ce=sum(p*u.entropy(ee)for p,bb,ee in branches)
                ic=cb-ce
                unused=u.optical_rate(a,b,budget)-u.optical_rate(a,b,mean)
                DB=u.thermal_entropy(a*mean)-sb;DE=u.thermal_entropy(b*mean)-se
                nonthermal=DB-DE;measuring=(sb-cb)-(se-ce)
                fullgap=u.optical_rate(a,b,budget)-ic
                self.assertAlmostEqual(fullgap,unused+nonthermal+measuring,places=12)
                self.assertGreaterEqual(min(unused,nonthermal,measuring),-4e-13)
                rows.append(dict(weights=[a,b,c],measurement=name,input_mean=mean,budget=budget,
                    coherent_information=ic,rate_gap=fullgap,unused_energy_penalty=unused,
                    nonthermal_penalty=nonthermal,measurement_penalty=measuring))
        # Ignoring all helper records leaves the full ED complement, not E alone.
        a,b,c=.2,.08,.72;q=.5;rho=np.diag([1-q,q]);V=u.splitter(a,b,c,1)
        full=V@rho@V.conj().T;B=u.ptrace(full,[2]*3,[0]);E=u.ptrace(full,[2]*3,[1]);ED=u.ptrace(full,[2]*3,[1,2])
        correct=u.entropy(B)-u.entropy(ED);incorrect=u.entropy(B)-u.entropy(E)
        _,bs=u.helper_branches(V,rho,np.eye(2),2);count=sum(p*(u.entropy(bb)-u.entropy(ee))for p,bb,ee in bs)
        self.assertLess(correct,0.);self.assertGreater(count,0.);self.assertLess(count,incorrect)
        self.assertAlmostEqual(correct,u.h2(a*q)-u.h2((1-a)*q),places=13)
        REPORT['three_nonnegative_penalties']={'records':rows,'coarse_record_control':{'correct_unmonitored_coherent_information':correct,'counted_coherent_information':count,'incorrect_inaccessible_only_subtraction':incorrect},
            'scope':'The decomposition concerns coherent information for a fixed refined helper measurement, not the achieved fidelity of a finite code. Coarse outcomes leave additional quantum information in the complement.'}

    def test_qubit_formula_has_one_root_or_one_entropy_crossover(self):
        rng=np.random.default_rng(710064);rows=[]
        weights=[(.2,.08),(.2,0.),(1.,0.),(.6,.4),(.8,.1),(.49,.48)]
        for _ in range(50):
            x=rng.dirichlet([1.3,1.1,1.2]);a=max(x[0],x[1]);b=min(x[0],x[1]);weights.append((a,b))
        for a,b in weights:
            q,rate,kind=qubit_optimum(a,b)
            if a<=b:continue
            kink=1/(1+a-b)
            left=minimize_scalar(lambda x:-rate_qubit(a,b,x),bounds=(0,kink),method='bounded',options={'xatol':1e-13})
            right=minimize_scalar(lambda x:-rate_qubit(a,b,x),bounds=(kink,1),method='bounded',options={'xatol':1e-13})
            independent=max(0.,-left.fun,-right.fun,rate_qubit(a,b,kink))
            self.assertLess(abs(rate-independent),2e-10)
            for x in (.01,.31,.61,.91):
                arg=x*kink
                self.assertAlmostEqual(rate_qubit(a,b,arg),u.h2(a*arg)-u.h2(b*arg),places=12)
            if a+b<1 and kink<1:
                probe=(1+kink)/2
                self.assertLessEqual(rate_qubit(a,b,probe),rate_qubit(a,b,kink)+2e-13)
            if len(rows)<10:rows.append(dict(a=a,b=b,q=q,rate=rate,mode=kind))
        q,rate,_=qubit_optimum(.2,.08)
        self.assertAlmostEqual(q,25/28,places=14)
        self.assertAlmostEqual(rate,.3057095431400063,places=13)
        REPORT['qubit_evaluation_rule']={'checked_weights':len(weights),'selected_records':rows,
            'scope':'An evaluation corollary of the unchanged qubit theorem, not an independently optimized helper measurement or a new physical model.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    if args.output.exists():parser.error('Refusing existing output')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
        scope='Finite proof-audit identities; original capacity formulas unchanged. Not independent scientific review.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful()else 1)
if __name__=='__main__':main()
