from basicAlogrism import *
from Euclid import *
import gmpy2

class RSA:
    p,q=0,0
    N=p*q
    e=65535
    m,c=0,0
    def Encrypt(self,m,p,q,e):
        self.p,self.q,self.e,self.m=p,q,e,m
        self.N=p*q
        return PowerMod(m,e,self.N)
    def Decrypt(self,c,p,q,e):
        dSolver=EnclidAlogrism()
        #return PowerMod(c,gmpy2.invert(e,(p-1)*(q-1)),p*q)
        return PowerMod(c,dSolver.inverseof(e,(p-1)*(q-1)),p*q)

