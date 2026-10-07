#!/usr/bin/env python3
"""Checks for the capacity audit and energy-constrained vacuum optical extension.

Usage: python check_audit.py --output NEW.json
Finite matrices test identities; the all-code capacity claims are analytical.
No prior scientific source is imported, and no output is overwritten.
"""
from __future__ import annotations
import argparse
import math
import json
from pathlib import Path
import unittest

import numpy as np
from scipy.special import xlogy
from scipy.stats import binom
import sympy as sp

REPORT: dict[str, object] = {}
LN2=math.log(2)


def entropy(rho):
    a=np.asarray(rho)
    e=a if a.ndim==1 else np.linalg.eigvalsh((a+a.conj().T)/2)
    assert float(np.min(e))>=-2e-12
    p=np.maximum(e.real,0.)
    return float(-np.sum(xlogy(p,p))/LN2)


def thermal_entropy(n):
    if n<0:raise ValueError('Mean energy must be nonnegative.')
    if n==0:return 0.
    # Stable at both large and small n.
    return float((math.log1p(n)+n*math.log1p(1/n))/LN2)


def h2(p):
    if not 0<=p<=1:raise ValueError('Probability outside [0,1].')
    return entropy(np.array([p,1-p]))


def optical_rate(a,b,n):
    if not (0<=a<=1 and 0<=b<=1 and a+b<=1+1e-14 and n>=0):
        raise ValueError('Require a,b>=0, a+b<=1 and mean input n>=0.')
    return 0. if a<=b else thermal_entropy(a*n)-thermal_entropy(b*n)


def ptrace(rho,dims,keep):
    dims=list(dims);keep=list(keep)
    assert keep==sorted(keep)
    t=np.asarray(rho).reshape(dims+dims)
    for axis in reversed([i for i in range(len(dims)) if i not in keep]):
        t=np.trace(t,axis1=axis,axis2=axis+len(dims))
        dims.pop(axis)
    n=math.prod(dims)
    return t.reshape(n,n)


def random_rho(d,rng):
    x=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    r=x@x.conj().T
    return r/np.trace(r)


def splitter(a,b,c,cut):
    d=cut+1;v=np.zeros((d,d,d,d),complex)
    for n in range(d):
        for i in range(n+1):
            for j in range(n-i+1):
                k=n-i-j
                v[i,j,k,n]=math.sqrt(math.factorial(n)/math.factorial(i)/math.factorial(j)/math.factorial(k)*a**i*b**j*c**k)
    return v.reshape(d**3,d)


def loss_kraus(t,d):
    if not 0<=t<=1:raise ValueError('Transmission outside [0,1].')
    ks=[]
    for l in range(d):
        k=np.zeros((d,d),complex)
        for n in range(l,d):k[n-l,n]=math.sqrt(math.comb(n,l)*(1-t)**l*t**(n-l))
        ks.append(k)
    return ks


def loss(rho,t):
    return sum(k@rho@k.conj().T for k in loss_kraus(t,len(rho)))


def local_loss(rho,t,d,site,modes):
    ans=np.zeros_like(rho,dtype=complex)
    for k in loss_kraus(t,d):
        K=np.ones((1,1),complex)
        for i in range(modes):K=np.kron(K,k if i==site else np.eye(d))
        ans+=K@rho@K.conj().T
    return ans


def loss_all(rho,t,d,modes):
    for site in range(modes):rho=local_loss(rho,t,d,site,modes)
    return rho


def helper_branches(v,rho,rows,d):
    full=v@rho@v.conj().T
    result=[]
    for row in rows:
        K=np.kron(np.eye(d*d),row.reshape(1,d))
        be=K@full@K.conj().T
        p=float(np.trace(be).real)
        if p>1e-14:
            result.append((p,ptrace(be,[d,d],[0])/p,ptrace(be,[d,d],[1])/p))
    return full,result


def thin(p,t):
    p=np.asarray(p,float);k=np.arange(len(p))[:,None];n=np.arange(len(p))[None,:]
    return binom.pmf(k,n,t)@p


def cutoff_thermal(n,cut):
    r=n/(1+n);tail=r**(cut+1)
    p=(1-r)*r**np.arange(cut+1)/(1-tail)
    return p,tail


def cutoff_entropy_bounds(s,n,cut):
    r=n/(1+n);tail=r**(cut+1)
    H=thermal_entropy(s*n)
    lower=max(0.,(H-h2(tail)-tail*thermal_entropy(s*(cut+1+n)))/(1-tail))
    upper=H/(1-tail)
    return lower,upper


class Checks(unittest.TestCase):
    def test_flagged_receiver_channel_and_two_converse_cuts(self):
        rng=np.random.default_rng(607101);records=[]
        for a,b,c in [(.2,.08,.72),(.4,.1,.5),(.2,0.,.8),(.3,.3,.4)]:
            for uses in [1,2]:
                V=splitter(a,b,c,1)
                if uses==2:
                    V=np.kron(V,V).reshape(2,2,2,2,2,2,4).transpose(0,3,1,4,2,5,6).reshape(64,4)
                d=2**uses;rho=random_rho(d,rng)
                z=rng.normal(size=(3*d,d))+1j*rng.normal(size=(3*d,d));rows,_=np.linalg.qr(z)
                self.assertLess(np.linalg.norm(rows.conj().T@rows-np.eye(d)),2e-14)
                full,bs=helper_branches(V,rho,rows,d)
                B=ptrace(full,[d,d,d],[0]);E=ptrace(full,[d,d,d],[1]);BD=ptrace(full,[d,d,d],[0,2])
                ic=sum(p*(entropy(bb)-entropy(ee))for p,bb,ee in bs)
                gaps=[entropy(B)-entropy(E)-ic,entropy(BD)-entropy(E)-ic]
                self.assertGreaterEqual(min(gaps),-2e-12)
                ks=loss_kraus(b/a,2)
                if uses==2:ks=[np.kron(k,l)for k in ks for l in ks]
                err=max(np.linalg.norm(sum(k@bb@k.conj().T for k in ks)-ee) for _,bb,ee in bs)
                self.assertLess(err,2e-13)
                if a==b:self.assertLess(abs(ic),1e-12)
                records.append(dict(weights=[a,b,c],uses=uses,outcomes=len(bs),coherent_information=ic,
                    two_cut_slacks=gaps,branch_simulation_error=float(err)))
        REPORT['receiver_only_flag_audit']={'records':records,'boundary':'The exact capacity achievability is from an ensemble theorem and constrained channel coding, not these finite random measurements.'}

    def test_marginal_degradation_is_insufficient(self):
        # Standard correctable random phase channel: helper reads its key.
        I=np.eye(2);Z=np.diag([1.,-1.]);V=np.zeros((2,2,2,2),complex)
        for i in range(2):
            V[:,0,0,i]=I[:,i]/math.sqrt(2)
            V[:,1,1,i]=Z[:,i]/math.sqrt(2)
        V=V.reshape(8,2);rng=np.random.default_rng(71);rows=[]
        for rho in [np.eye(2)/2,random_rho(2,rng),np.array([[1.,0.],[0.,0.]])]:
            out=V@rho@V.conj().T
            E=ptrace(out,[2,2,2],[1]);B=ptrace(out,[2,2,2],[0])
            self.assertLess(np.linalg.norm(E-np.eye(2)/2),2e-14)
            self.assertLess(np.linalg.norm(B-np.diag(np.diag(rho))),2e-14)
            recovered=np.zeros((2,2),complex)
            for k,U in enumerate([I,Z]):
                K=np.kron(np.eye(4),np.eye(2)[k:k+1]);be=K@out@K.conj().T
                recovered+=U@ptrace(be,[2,2],[0])@U.conj().T
            self.assertLess(np.linalg.norm(recovered-rho),2e-14)
            rows.append({'input_entropy':entropy(rho),'first_cut_without_required_hypothesis':entropy(B)-entropy(E),
                         'recovery_error':float(np.linalg.norm(recovered-rho))})
        # The input matrix |0><0| has ED coherence but BD has no D coherence.
        out=np.outer(V[:,0],V[:,0].conj());ED=ptrace(out,[2,2,2],[1,2]);BD=ptrace(out,[2,2,2],[0,2])
        self.assertAlmostEqual(abs(ED[0,3]),.5,places=14)
        self.assertEqual(np.linalg.norm(BD.reshape(2,2,2,2)[:,0,:,1]),0.)
        REPORT['hypothesis_countercontrol']={'rows':rows,'helper_corrected_capacity':1,
            'maximum_false_marginal_cut':0,'explanation':'E is a replacement of B marginally; no map on B alone can create the missing D off-diagonal blocks. This is an inherited random-unitary correction mechanism, not a new effect.'}

    def test_passive_fock_identity_and_conditioning(self):
        rng=np.random.default_rng(11071);records=[]
        for cut in [2,3,4]:
            d=cut+1;a,b,c=.3,.1,.6;V=splitter(a,b,c,cut)
            self.assertLess(np.linalg.norm(V.conj().T@V-np.eye(d)),3e-14)
            rho=random_rho(d,rng);out=V@rho@V.conj().T
            B=ptrace(out,[d]*3,[0]);E=ptrace(out,[d]*3,[1]);BD=ptrace(out,[d]*3,[0,2]);ED=ptrace(out,[d]*3,[1,2])
            sim=local_loss(BD,b/a,d,0,2)
            self.assertLess(np.linalg.norm(sim-ED),2e-13)
            self.assertLess(np.linalg.norm(B-loss(rho,a)),2e-13)
            self.assertLess(np.linalg.norm(E-loss(rho,b)),2e-13)
            z=rng.normal(size=(2*d,d))+1j*rng.normal(size=(2*d,d));Q,_=np.linalg.qr(z)
            _,branches=helper_branches(V,rho,Q,d)
            for p,bb,ee in branches:self.assertLess(np.linalg.norm(loss(bb,b/a)-ee),2e-13)
            records.append(dict(cut=cut,input_mean=float(np.dot(np.arange(d),np.diag(rho).real)),
                                identity_error=float(np.linalg.norm(sim-ED)),conditional_outcomes=len(branches)))
        REPORT['exact_finite_sectors']={'records':records,'boundary':'Finite total-excitation sectors are exact and closed. They verify identities, not the infinite-dimensional capacity by cutoff extrapolation.'}

    def test_thermal_extremality_for_nongaussian_entangled_inputs(self):
        rng=np.random.default_rng(8071);records=[]
        for modes,d in [(1,5),(2,4)]:
            n_op=np.zeros((d**modes,d**modes))
            for site in range(modes):
                M=np.ones((1,1))
                for i in range(modes):M=np.kron(M,np.diag(np.arange(d)) if i==site else np.eye(d))
                n_op+=M
            for a,b in [(.2,.08),(.7,.2),(.2,0.)]:
                for sample in range(4):
                    rho=random_rho(d**modes,rng)
                    B=loss_all(rho,a,d,modes);E=loss_all(rho,b,d,modes)
                    mean=float(np.trace(rho@n_op).real)/modes
                    EB=float(np.trace(B@n_op).real);EE=float(np.trace(E@n_op).real)
                    self.assertAlmostEqual(EB,modes*a*mean,places=12);self.assertAlmostEqual(EE,modes*b*mean,places=12)
                    DB=modes*math.log2(1+a*mean)+EB*math.log2(1+1/(a*mean))-entropy(B)
                    DE=0. if b==0 else modes*math.log2(1+b*mean)+EE*math.log2(1+1/(b*mean))-entropy(E)
                    diff=entropy(B)-entropy(E);cap=modes*optical_rate(a,b,mean)
                    self.assertAlmostEqual(cap-diff,DB-DE,places=11)
                    self.assertGreaterEqual(DB-DE,-2e-12)
                    self.assertLessEqual(diff,cap+2e-12)
                    if sample==0:records.append(dict(modes=modes,local_cut=d-1,a=a,b=b,mean_per_mode=mean,
                        entropy_difference=diff,upper_bound=cap,relative_entropy_gap=DB-DE))
        REPORT['arbitrary_input_entropy_bound']={'records':records,
            'proof':'The infinite thermal reference is evaluated through log tau, never replaced by a renormalized finite thermal matrix. Relative-entropy contraction gives the all-input/all-use analytical inequality.'}

    def test_thermal_cutoff_achievability_with_charged_energy(self):
        records=[]
        for a,b,c,n in [(.2,.08,.72,1.),(.6,.1,.3,3.),(.2,0.,.8,1.),(.2,.16,.64,.1)]:
            exact=optical_rate(a,b,n);data=[]
            for cut in [4,12,40,120]:
                p,tail=cutoff_thermal(n,cut);mean=float(np.dot(p,np.arange(cut+1)))
                self.assertAlmostEqual(mean,n-(cut+1)*tail/(1-tail),places=11)
                self.assertLessEqual(mean,n+2e-14)
                values={s:entropy(thin(p,s))for s in [a,b,1-b]}
                intervals={s:cutoff_entropy_bounds(s,n,cut)for s in values}
                for s,H in values.items():
                    lo,hi=intervals[s];self.assertGreaterEqual(H,lo-2e-12);self.assertLessEqual(H,hi+2e-12)
                rate=min(values[a],values[1-b])-values[b]
                cert=min(intervals[a][0],intervals[1-b][0])-intervals[b][1]
                self.assertGreaterEqual(rate,cert-2e-12);self.assertLessEqual(rate,optical_rate(a,b,mean)+2e-12)
                self.assertLessEqual(rate,exact+2e-12)
                data.append(dict(cut=cut,thermal_tail=tail,mean_input=mean,finite_input_min_cut_rate=rate,
                                 analytic_lower_enclosure=max(0.,cert),distance_to_infinite_formula=exact-rate))
            self.assertLess(abs(data[-1]['finite_input_min_cut_rate']-exact),5e-12)
            self.assertLess(exact-data[-1]['analytic_lower_enclosure'],2e-11)
            records.append(dict(weights=[a,b,c],mean_budget=n,capacity=exact,cutoffs=data))
        REPORT['energy_constrained_achievability']={'records':records,
            'boundary':'The displayed finite-input rate uses established block assistance and subsequent channel coding. No finite-block receiver is simulated. Truncation is an analytical achievability step, not a physical restriction in the converse.'}

    def test_energy_law_limits_and_resource_comparators(self):
        n,a,b=sp.symbols('n a b',positive=True)
        G=lambda x:((x+1)*sp.log(x+1)-x*sp.log(x))/sp.log(2)
        f=G(a*n)-G(b*n)
        second=sp.simplify(sp.diff(f,n,2))
        self.assertEqual(sp.simplify(second-(b-a)/(sp.log(2)*n*(1+a*n)*(1+b*n))),0)
        records=[]
        for eta in [.5,.75,.8,.9,1.]:
            aa=.2;bb=.8*(1-eta);cc=.8*eta
            for N in [1.,10.]:
                value=optical_rate(aa,bb,N)
                if eta<=.75:self.assertLess(abs(value),5e-15)
                coherent=optical_rate(1-bb,bb,N)
                self.assertLessEqual(value,coherent+2e-14)
                records.append(dict(decay=.8,collection=eta,mean_input=N,measurement_assisted_capacity=value,
                    coherent_collection_capacity=coherent,unmonitored_capacity=optical_rate(aa,1-aa,N)))
        limits=[]
        for aa,bb in [(.2,.08),(.4,.1),(.51,.49)]:
            capinf=math.log2(aa/bb);ns=[1.,10.,1e3,1e6];ys=[optical_rate(aa,bb,N)for N in ns]
            self.assertTrue(all(x<y for x,y in zip(ys,ys[1:])))
            self.assertTrue(all(y<capinf for y in ys));self.assertLess(capinf-ys[-1],1e-5)
            limits.append(dict(a=aa,b=bb,energy=ns,rates=ys,unbounded_energy_supremum=capinf))
        # Same rate as a known pure-loss formula after rescaling the energy; not a physical channel simulation.
        for aa,bb,N in [(.2,.08,1.),(.4,.1,3.),(.7,.2,.1)]:
            self.assertAlmostEqual(optical_rate(aa,bb,N),optical_rate(aa/(aa+bb),bb/(aa+bb),(aa+bb)*N),places=13)
        REPORT['closed_energy_law']={'table':records,'large_energy':limits,
          'curvature':'(b-a)/(ln(2)*N*(1+a*N)*(1+b*N))',
          'resource_boundary':'Input photon budget only. Helper collective quantum processing, phase reference and classical messages are allowed; no nonvacuum incoming environment, quantum helper-to-receiver transmission, or two-way distillation.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():p.error('Refuse existing output')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS'if result.wasSuccessful()else'FAIL',groups=result.testsRun,
        scope='Author-side analytical-theorem checks, not priority certification or independent peer review.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful()else 1)
if __name__=='__main__':main()
