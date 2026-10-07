#!/usr/bin/env python3
"""Seven bounded channel checks; analytical all-block statements are in FOLLOWUP.md.
Usage: python check_monitoring_followup.py --output NEW.json
"""
from __future__ import annotations
import argparse, json, math, sys, unittest
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar,brentq

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'prior'))
from check_monitoring import entropy,se,capacity,isometry,partial_trace,ad_kraus,on_middle
REPORT={}
h=lambda q:entropy([q,1-q])

def ad(r,s):return sum(k@r@k.conj().T for k in ad_kraus(s))
def rates_upper(a,b):
    if a<=b:return 0.,0.
    # h(q) and d(q) concave. Locate their crossing and smooth stationary candidates.
    d=lambda q:h(a*q)-h(b*q)
    cross=1. if a+b==1. else brentq(lambda q:h(q)-d(q),1e-10,1-1e-12,xtol=1e-14)
    obj=lambda q:min(h(q),d(q))
    opt=minimize_scalar(lambda q:-d(q),bounds=(1e-12,cross),method='bounded',options={'xatol':1e-14})
    qs=[0.,.5,cross,float(opt.x),1.]
    q=max(qs,key=obj)
    return float(obj(q)),float(q)

def exact_capacity(a,b,c):
    """Numerically maximize the proved single-letter formula; no POVM search.

    Splitting at the entropy-branch crossing avoids a nondifferentiable objective.
    Numerical maxima are not interval certificates for the reported decimals.
    """
    if min(a,b,c)<-1e-14 or abs(a+b+c-1)>1e-12:
        raise ValueError('Require a,b,c>=0 and a+b+c=1.')
    if a<=b:return 0.,0.
    cut=1/(1+a-b)
    f=lambda q:min(h(a*q),h((1-b)*q))-h(b*q)
    candidates=[0.,cut,1.]
    for lo,hi in [(0.,cut),(cut,1.)]:
        if hi-lo>1e-12:
            opt=minimize_scalar(lambda q:-f(q),bounds=(lo,hi),method='bounded',options={'xatol':1e-14})
            candidates.append(float(opt.x))
    q=max(candidates,key=f)
    return float(f(q)),float(q)

def isometry_n(a,b,c,n):
    V=isometry(a,b,c)
    if n==1:return V
    # Group B1 B2, E1 E2, D1 D2, and preserve input tensor order.
    return np.kron(V,V).reshape(2,2,2,2,2,2,4).transpose(0,3,1,4,2,5,6).reshape(64,4)

def ensemble(V,rho,dim,rows):
    out=V@rho@V.conj().T
    b=partial_trace(out,[dim]*3,[0]);e=partial_trace(out,[dim]*3,[1])
    bd=partial_trace(out,[dim]*3,[0,2])
    bx=[];ex=[];weights=[]
    for row in rows:
        K=np.kron(np.eye(dim*dim),row.reshape(1,dim))
        sub=K@out@K.conj().T
        bb=partial_trace(sub,[dim,dim],[0]);ee=partial_trace(sub,[dim,dim],[1])
        p=float(np.trace(bb).real)
        if p>1e-14:bx.append(bb/p);ex.append(ee/p);weights.append(p)
    return b,e,bd,weights,bx,ex

def random_povm(d,m,rng):
    Z=rng.normal(size=(m,d))+1j*rng.normal(size=(m,d));Q,_=np.linalg.qr(Z)
    return Q # rows are bras; sum row^dagger row=I

def fock_isometry(a,b,c,cut):
    d=cut+1;V=np.zeros((d,d,d,d),complex)
    for n in range(d):
        for i in range(n+1):
            for j in range(n-i+1):
                k=n-i-j
                V[i,j,k,n]=math.sqrt(math.factorial(n)/(math.factorial(i)*math.factorial(j)*math.factorial(k))*a**i*b**j*c**k)
    return V.reshape(d**3,d)

def loss_kraus(s,cut):
    d=cut+1;out=[]
    for lost in range(d):
        K=np.zeros((d,d))
        for n in range(lost,d):K[n-lost,n]=math.sqrt(math.comb(n,lost)*(1-s)**lost*s**(n-lost))
        out.append(K)
    return out

class Checks(unittest.TestCase):
    def test_reverse_simulation_and_classical_information_penalty(self):
        rng=np.random.default_rng(61061);rows=[]
        for a,b,c in [(.2,.08,.72),(.6,.1,.3),(.2,0.,.8),(.4,.4,.2)]:
            for n in [1,2]:
                d=2**n;V=isometry_n(a,b,c,n)
                M=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));rho=M@M.conj().T;rho/=np.trace(rho)
                Q=random_povm(d,2*d,rng)
                B,E,BD,p,Bx,Ex=ensemble(V,rho,d,Q)
                ks=ad_kraus(b/a)
                if n==2:ks=[np.kron(x,y)for x in ks for y in ks]
                for bb,ee in zip(Bx,Ex):self.assertLess(np.linalg.norm(sum(k@bb@k.conj().T for k in ks)-ee),3e-13)
                ic=sum(w*(se(bb)-se(ee))for w,bb,ee in zip(p,Bx,Ex))
                difference=se(B)-se(E)
                loss=(se(B)-sum(w*se(bb)for w,bb in zip(p,Bx)))-(se(E)-sum(w*se(ee)for w,ee in zip(p,Ex)))
                self.assertGreaterEqual(loss,-3e-13)
                self.assertAlmostEqual(difference-ic,loss,places=12)
                second_cut=se(BD)-se(E)
                self.assertLessEqual(ic,min(second_cut,difference)+4e-13)
                self.assertLessEqual(second_cut,se(rho)+4e-13)
                # Input-entropy and receiver-minus-loss-entropy bounds reduce to single sites.
                dm=[];sh=[];bdm=[]
                for i in range(n):
                    ri=rho if n==1 else partial_trace(rho,[2,2],[i])
                    dm.append(se(ad(ri,a))-se(ad(ri,b)));sh.append(se(ri))
                    bdm.append(se(ad(ri,1-b))-se(ad(ri,b)))
                self.assertLessEqual(difference,sum(dm)+4e-13)
                self.assertLessEqual(se(rho),sum(sh)+4e-13)
                self.assertLessEqual(second_cut,sum(bdm)+4e-13)
                average=rho if n==1 else (partial_trace(rho,[2,2],[0])+partial_trace(rho,[2,2],[1]))/2
                average_cuts=[se(ad(average,survival))-se(ad(average,b)) for survival in (a,1-b)]
                self.assertLessEqual(min(sum(dm),sum(bdm)),n*min(average_cuts)+4e-13)
                U,q=exact_capacity(a,b,c)
                self.assertLessEqual(ic,n*U+1e-10)
                rows.append(dict(a=a,b=b,c=c,uses=n,helper_outcomes=2*d,coherent_information=ic,
                    entropy_difference=difference,second_cut=second_cut,classical_record_penalty=loss,
                    exact_capacity_per_use=U,proof_boundary="Attainment uses the cited asymptotic assistance/coding theorem, not this finite POVM test.")))
        REPORT['collective_helper_entropy_bound']=rows

    def test_exact_capacity_limits_and_threshold_slopes(self):
        rows=[]
        for eta in [.75,.751,.76,.8,.9,1.]:
            a=.2;b=.8*(1-eta);c=.8*eta
            lower,qlo=capacity(a,b,c);upper,qup=exact_capacity(a,b,c)
            self.assertGreaterEqual(upper+2e-12,lower)
            if eta==1:self.assertAlmostEqual(upper,h(1/6),places=11)
            rows.append(dict(decay=.8,collection=eta,counting_capacity=lower,exact_monitored_capacity=upper,
                             counting_optimum_population=qlo,monitored_optimum_population=qup))
        # Near-threshold slopes for counting and the newly proved exact monitored capacity.
        t=.2
        fl=lambda q:0. if q==0 else q*np.log2((1-(1-t)*q)/(t*q))
        lower_opt=minimize_scalar(lambda q:-fl(q),bounds=(1e-12,1-1e-12),method='bounded')
        slope_lower=float(-lower_opt.fun);slope_upper=2.
        edge=[]
        for eps in [1e-2,1e-3,1e-4]:
            a=t+eps/2;b=t-eps/2
            L=capacity(a,b,.6)[0];U=exact_capacity(a,b,.6)[0]
            edge.append(dict(epsilon=eps,lower_over_epsilon=L/eps,upper_over_epsilon=U/eps))
        self.assertLess(abs(edge[-1]['lower_over_epsilon']-slope_lower),1e-7)
        self.assertLess(abs(edge[-1]['upper_over_epsilon']-slope_upper),1e-5)
        for a in [.55,.8,1.]:
            upper,_=exact_capacity(a,1-a,0.)
            self.assertAlmostEqual(upper,capacity(a,1-a,0)[0],places=10)
        REPORT['exact_rate_formula']={'rows':rows,'threshold_path':'a=.2+epsilon/2, b=.2-epsilon/2, c=.6',
             'lower_slope':slope_lower,'upper_slope':slope_upper,'edge_checks':edge,
             'boundary':'The formula is analytically proved using register-preserving degradation plus established asymptotic assistance. Its scalar optimization is numerical; no finite-size helper or practical decoder is supplied.'}

    def test_message_fidelity_operator_bound(self):
        rows=[]
        for d in [2,3,4,6]:
            ph=np.eye(d).reshape(-1)/np.sqrt(d);P=np.outer(ph,ph)
            A=np.kron(P,np.eye(d))
            # A acts R,B; B acts R,Bprime.
            B=A.reshape(d,d,d,d,d,d).transpose(0,2,1,3,5,4).reshape(d**3,d**3)
            maximum=float(np.linalg.eigvalsh(A+B)[-1]);expected=1+1/d
            self.assertAlmostEqual(maximum,expected,places=12)
            rows.append(dict(message_dimension=d,projector_sum_norm=maximum,
                             entanglement_fidelity_ceiling=(1+1/d)/2))
        REPORT['finite_message_ceiling']={'rows':rows,'scope':'Standard two-extension/no-cloning ceiling applied to each arbitrary block helper channel; no finite-block code achieves this bound asserted.'}

    def test_bosonic_vacuum_extension_all_fock_coherences(self):
        rows=[]
        for cut in [2,3,4]:
            d=cut+1
            for a,b,c in [(.1,.2,.7),(.2,.2,.6),(.4,.1,.5)]:
                V=fock_isometry(a,b,c,cut)
                self.assertLess(np.linalg.norm(V.conj().T@V-np.eye(d)),1e-13)
                left,right=(0,1) if a<=b else (1,0)
                transmission=min(a,b)/max(a,b);ks=loss_kraus(transmission,cut)
                maximum=0.
                for i in range(d):
                    for j in range(d):
                        op=np.outer(V[:,i],V[:,j].conj())
                        target=partial_trace(op,[d]*3,[left,2]);origin=partial_trace(op,[d]*3,[right,2])
                        sim=sum(np.kron(k,np.eye(d))@origin@np.kron(k.T,np.eye(d))for k in ks)
                        maximum=max(maximum,float(np.linalg.norm(target-sim)))
                self.assertLess(maximum,2e-13)
                rows.append(dict(max_input_photons=cut,a=a,b=b,c=c,matrix_unit_error=maximum))
        REPORT['bosonic_extension']={'rows':rows,'proof':'Coherent-input dyads or passive dilation prove the identity on full Fock space; exact finite excitation sectors are only tests.',
           'scope':'Vacuum passive splitting and helper output measurement; excludes prepared nonvacuum bath inputs, two-way assistance and in-flight feedback.'}

    def test_counted_achievability_under_arbitrary_positive_energy_budget(self):
        rows=[]
        for cap in [1e-4,.001,.01,.1]:
            # A positive excited population <= budget gives positive coherent info.
            q=min(cap/2,.01);a,b,c=.2,.08,.72
            from check_monitoring import ci_diag
            value=ci_diag(q,a,b,c)
            self.assertGreater(value,0.)
            rows.append(dict(mean_excitation_budget=cap,chosen_population=q,achievable_coherent_information=value))
        REPORT['finite_energy_positivity']=rows

    def test_concavity_and_phase_twirl_for_entropy_bound(self):
        rng=np.random.default_rng(441);maxerr=0.
        for _ in range(100):
            vals=np.sort(rng.dirichlet([1,1,1])[:2]);b,a=vals
            states=[]
            for j in range(2):
                Z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));r=Z@Z.conj().T;r/=np.trace(r);states.append(r)
            mix=.37*states[0]+.63*states[1]
            diag=np.diag(np.diag(mix))
            for survival in (a,1-b):
                D=lambda r:se(ad(r,survival))-se(ad(r,b))
                self.assertGreaterEqual(D(mix)-.37*D(states[0])-.63*D(states[1]),-1e-12)
                self.assertGreaterEqual(D(diag)-D(mix),-1e-12)
            self.assertGreaterEqual(se(diag)-se(mix),-1e-12)
        REPORT['entropy_reduction']='100 deterministic random tests of proven degraded-entropy concavity and phase twirling; finite tests not their proof.'

    def test_two_cut_entropy_formula_and_corrected_partial_rate(self):
        rows=[]
        for a,b,c in [(.2,.08,.72),(.2,.16,.64),(.8,.2,0.),(.2,0.,.8),(1.,0.,0.),(.5,.5,0.)]:
            V=isometry(a,b,c)
            for q in [.01,.2,.5,.85,1.]:
                rho=np.diag([1-q,q]);out=V@rho@V.conj().T
                B=partial_trace(out,[2,2,2],[0]);E=partial_trace(out,[2,2,2],[1]);BD=partial_trace(out,[2,2,2],[0,2])
                first=se(B)-se(E);second=se(BD)-se(E)
                formula=min(h(a*q),h((1-b)*q))-h(b*q)
                self.assertAlmostEqual(min(first,second),formula,places=12)
                self.assertLessEqual(second,se(rho)+1e-12)
            value,qopt=exact_capacity(a,b,c)
            loose,unused=rates_upper(a,b)
            self.assertLessEqual(value,loose+2e-12)
            self.assertGreaterEqual(value+2e-12,capacity(a,b,c)[0])
            grid=np.linspace(0,1,2001)
            best=max(min(h(a*q),h((1-b)*q))-h(b*q)for q in grid)
            self.assertGreaterEqual(value+1e-10,best)
            rows.append(dict(a=a,b=b,c=c,exact_capacity=value,optimal_population=qopt,                earlier_loose_bound=loose,grid_lower=best))
        exact,qopt=exact_capacity(.2,.08,.72)
        self.assertAlmostEqual(qopt,25/28,places=12)
        self.assertAlmostEqual(exact,h(5/28)-h(1/14),places=12)
        self.assertAlmostEqual(exact,.3057095431400063,places=12)
        self.assertLess(exact,rates_upper(.2,.08)[0]-.005)
        self.assertAlmostEqual(exact_capacity(1.,0.,0.)[0],1.,places=12)
        REPORT['two_cut_identity_and_rate_control']=rows

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    if args.output.exists():p.error('Refusing existing output')
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS'if r.wasSuccessful()else'FAIL',test_groups=r.testsRun)
    args.output.parent.mkdir(exist_ok=True,parents=True)
    with args.output.open('x')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if r.wasSuccessful()else 1)
