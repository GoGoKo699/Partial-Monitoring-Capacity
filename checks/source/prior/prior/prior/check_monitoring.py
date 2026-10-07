#!/usr/bin/env python3
"""Exact finite channel identities and small diagnostics for partial monitoring.
Run with --output NEW.json. No prior project code is read.
"""
from __future__ import annotations
import argparse, json, unittest
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar
from scipy.special import xlogy

REPORT={}

def entropy(p):
    p=np.asarray(p,dtype=float)
    if p.min() < -1e-10: raise ValueError('Negative spectrum')
    p=np.maximum(p,0.)
    return float(-np.sum(xlogy(p,p))/np.log(2))

def se(r): return entropy(np.linalg.eigvalsh((r+r.conj().T)/2))

def channel(r,a,b,c):
    return np.array([[r[0,0]+b*r[1,1],np.sqrt(a)*r[0,1],0],
                     [np.sqrt(a)*r[1,0],a*r[1,1],0],[0,0,c*r[1,1]]],complex)

def isometry(a,b,c):
    V=np.zeros((2,2,2,2),complex) # B,E,D,input
    V[0,0,0,0]=1
    V[1,0,0,1]=np.sqrt(a); V[0,1,0,1]=np.sqrt(b); V[0,0,1,1]=np.sqrt(c)
    return V.reshape(8,2)

def partial_trace(r,dims,keep):
    dims=list(dims); keep=list(keep)
    t=r.reshape(dims+dims)
    for i in sorted(set(range(len(dims)))-set(keep),reverse=True):
        t=np.trace(t,axis1=i,axis2=i+len(dims)); dims.pop(i)
    return t.reshape(np.prod(dims),np.prod(dims))

def ad_kraus(s):
    return [np.diag([1,np.sqrt(s)]),np.array([[0,np.sqrt(1-s)],[0,0]])]

def on_middle(r,dleft,dright,kraus):
    return sum((np.kron(np.eye(dleft),np.kron(k,np.eye(dright)))@r@
                np.kron(np.eye(dleft),np.kron(k.conj().T,np.eye(dright)))) for k in kraus)

def flagged_degrade(r,t):
    k0=np.diag([1,np.sqrt(t),1]); k1=np.zeros((3,3));k1[0,1]=np.sqrt(1-t)
    return k0@r@k0.conj().T+k1@r@k1.conj().T

def ci_diag(q,a,b,c):
    return entropy([1-(a+c)*q,a*q,c*q])-entropy([1-(b+c)*q,b*q,c*q])

def capacity(a,b,c):
    if a<=b+1e-14:return 0.,None
    opt=minimize_scalar(lambda q:-ci_diag(q,a,b,c),bounds=(1e-12,1-1e-12),
                        method='bounded',options={'xatol':1e-13})
    return float(-opt.fun),float(opt.x)

def choi_joint(a,b,c,n=1):
    V=isometry(a,b,c)
    if n==2:
        V=np.kron(V,V).reshape(2,2,2,2,2,2,4).transpose(0,3,1,4,2,5,6).reshape(64,4)
    d=2**n
    vec=V.T.reshape(-1)/np.sqrt(d) # reference, B,E,D
    r=np.outer(vec,vec.conj())
    return (partial_trace(r,[d,d,d,d],[0,1,3]),partial_trace(r,[d,d,d,d],[0,2,3]))

class MonitoringChecks(unittest.TestCase):
    def test_flagged_channel_and_complement_exact(self):
        a,b,c,x,y,u,v=sp.symbols('a b c x y u v',nonnegative=True)
        K0=sp.Matrix([[1,0],[0,sp.sqrt(a)],[0,0]])
        K1=sp.Matrix([[0,sp.sqrt(b)],[0,0],[0,0]])
        K2=sp.Matrix([[0,0],[0,0],[0,sp.sqrt(c)]])
        Ks=[K0,K1,K2];rho=sp.Matrix([[x,u+sp.I*v],[u-sp.I*v,y]])
        out=sum((k*rho*k.conjugate().T for k in Ks),sp.zeros(3))
        comp=sp.Matrix(3,3,lambda i,j:sp.trace(Ks[i]*rho*Ks[j].conjugate().T))
        target=sp.Matrix([[x+b*y,sp.sqrt(a)*(u+sp.I*v),0],[sp.sqrt(a)*(u-sp.I*v),a*y,0],[0,0,c*y]])
        complement=sp.Matrix([[x+a*y,sp.sqrt(b)*(u+sp.I*v),0],[sp.sqrt(b)*(u-sp.I*v),b*y,0],[0,0,c*y]])
        self.assertEqual(sp.simplify(out-target),sp.zeros(3))
        self.assertEqual(sp.simplify(comp-complement),sp.zeros(3))
        self.assertEqual(sum((k.conjugate().T*k for k in Ks),sp.zeros(2)),sp.diag(1,a+b+c))
        REPORT['kraus']='Exact symbolic output/complement swap a<->b; trace preservation when a+b+c=1.'

    def test_degradability_and_antidegradability(self):
        rng=np.random.default_rng(1006);maxerr=0.
        for _ in range(80):
            a,b,c=rng.dirichlet([1,1,1]);M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
            r=M@M.conj().T;r/=np.trace(r)
            B=channel(r,a,b,c);E=channel(r,b,a,c)
            if a>=b: err=np.linalg.norm(flagged_degrade(B,b/a)-E)
            else: err=np.linalg.norm(flagged_degrade(E,a/b)-B)
            maxerr=max(maxerr,float(err));self.assertLess(err,2e-14)
        REPORT['degradability']={'tests':80,'maximum_error':maxerr,'proof':'Explicit amplitude damping on nonflag block; click flag preserved.'}

    def test_register_preserving_converse_before_any_measurement(self):
        rows=[]
        for a,b,c in [(0.1,0.2,0.7),(0.2,0.2,0.6),(0.,.4,.6)]:
            for n in (1,2):
                B,E=choi_joint(a,b,c,n);d=2**n
                ks=ad_kraus(a/b)
                if n==2:ks=[np.kron(i,j)for i in ks for j in ks]
                transformed=on_middle(E,d,d,ks)
                err=float(np.linalg.norm(B-transformed));self.assertLess(err,2e-14)
                # Entangled measurement basis across the two collected emissions.
                rng=np.random.default_rng(19+n)
                Z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));Q,_=np.linalg.qr(Z)
                brancherr=0.
                for j in range(d):
                    m=np.kron(np.eye(d*d),Q[:,j].conj().reshape(1,d))
                    bb=m@B@m.conj().T;ee=m@E@m.conj().T
                    brancherr=max(brancherr,float(np.linalg.norm(bb-on_middle(ee,d,1,ks))))
                self.assertLess(brancherr,2e-14)
                rows.append({'a':a,'b':b,'c':c,'uses':n,'choi_error':err,'measurement_branch_error':brancherr})
        REPORT['universal_monitoring_converse']={'rows':rows,'scope':'Choi identities check reference preservation before measuring D. Tensorization and commuting any instrument with the degrading map prove the all-blocklength statement; finite tests do not prove it by enumeration.'}

    def test_capacity_formula_and_phase_twirl(self):
        rng=np.random.default_rng(61);rows=[]
        for r,eta in [(0.,.5),(.8,.5),(.8,.75),(.8,.8),(.8,.9),(.8,1.),(.9,.95)]:
            a,b,c=1-r,r*(1-eta),r*eta
            val,q=capacity(a,b,c)
            self.assertGreaterEqual(val,0.);self.assertLessEqual(val,1+1e-12)
            if a>b+1e-12:
                for _ in range(40):
                    M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));rho=M@M.conj().T;rho/=np.trace(rho)
                    ic=se(channel(rho,a,b,c))-se(channel(rho,b,a,c))
                    diagonal=ci_diag(float(rho[1,1].real),a,b,c)
                    self.assertLessEqual(ic,diagonal+2e-13)
                    self.assertLessEqual(diagonal,val+2e-12)
            rows.append({'decay_probability':r,'collection':eta,'count_capacity':val,'optimal_excited_population':q})
        self.assertAlmostEqual(capacity(.2,.08,.72)[0],.18621044456571,places=11)
        self.assertAlmostEqual(capacity(1,0,0)[0],1.,places=13)
        self.assertEqual(capacity(.2,.2,.6)[0],0.)
        REPORT['counting_capacity']={'rows':rows,'scope':'Analytic degradability/phase covariance gives single-letter optimization. Reported interior maxima are scalar numerical evaluations, not interval certificates.'}

    def test_quantum_access_control_and_residual_entanglement(self):
        a,b,c=.1,.2,.7;V=isometry(a,b,c)
        embed=np.zeros((4,2));embed[0,0]=1
        embed[2,1]=np.sqrt(a/(a+c));embed[1,1]=np.sqrt(c/(a+c))
        rng=np.random.default_rng(4);maximum=0.
        for _ in range(12):
            z=rng.normal(size=2)+1j*rng.normal(size=2);z/=np.linalg.norm(z);rho=np.outer(z,z.conj())
            out=partial_trace(V@rho@V.conj().T,[2,2,2],[0,2])
            expected=embed@sum(k@rho@k.conj().T for k in ad_kraus(1-b))@embed.T
            maximum=max(maximum,float(np.linalg.norm(out-expected)))
        self.assertLess(maximum,2e-14)
        # Counting-channel Choi partial transpose is nonpositive even though Q=0.
        psi=np.array([1,0,0,1])/np.sqrt(2);rr=np.outer(psi,psi)
        choi=np.block([[channel(rr[:2,:2],a,b,c),channel(rr[:2,2:],a,b,c)],
                       [channel(rr[2:,:2],a,b,c),channel(rr[2:,2:],a,b,c)]])
        pt=choi.reshape(2,3,2,3).transpose(2,1,0,3).reshape(6,6)
        neg=-np.linalg.eigvalsh(pt)[0]
        self.assertAlmostEqual(neg,(np.sqrt(b*b+4*a)-b)/4,places=13)
        self.assertGreater(neg,0.)
        REPORT['coherent_collection_control']={'a':a,'b':b,'c':c,'all_classical_monitoring_capacity':0,
            'quantum_collection_capacity':capacity(1-b,b,0)[0],'channel_identity_error':maximum,
            'counted_choi_negativity':float(neg),'boundary':'Zero unassisted quantum rate is not an entanglement-breaking claim; two-way assisted tasks are different.'}

    def test_lifetime_boundary_and_click_information_not_global_optimum(self):
        rows=[]
        for eta in (0.,.5,.8,.9,.99):
            tau=np.log((2-eta)/(1-eta))
            decay=1-np.exp(-tau)
            self.assertAlmostEqual(1-decay,decay*(1-eta),places=13)
            rows.append({'collection':eta,'critical_Gamma_t':float(tau),'ratio_to_unmonitored':float(tau/np.log(2))})
        # Complete-environment collective measurement already has a larger capacity
        # than per-use counting (standard entanglement-of-assistance theorem).
        a=.2
        assisted=entropy([a/(1+a),1/(1+a)])
        counted,_=capacity(a,0,1-a)
        self.assertGreater(assisted,counted)
        REPORT['lifetime_and_scope']={'rows':rows,'full_collection_example':{'survival':a,'counting_capacity':counted,
            'known_full_environment_assisted_capacity':assisted},
            'boundary':'Threshold is optimized over measurement-only helper strategies; counting rate itself is not claimed globally optimal over such measurements. No intervention during decay.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():p.error('Refusing existing report')
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(MonitoringChecks))
    REPORT.update(status='PASS'if r.wasSuccessful()else'FAIL',test_groups=r.testsRun)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if r.wasSuccessful()else 1)
