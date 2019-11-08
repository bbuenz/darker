import gmpy2, random
from gmpy2 import mpz, mpq, mpfr, mpc

import numpy.polynomial

class rsaelement:


    def __init__(self,value=mpz(2),n=None):
        if n == None:
            p = gmpy2.next_prime(random.getrandbits(256))
            q = gmpy2.next_prime(random.getrandbits(256))
            n = p * q
        self.n=n
        self.value= gmpy2.f_mod(value,self.n)
    def __mul__(self, other):
        if self.n != other.n:
            raise
        else:
            return rsaelement(gmpy2.fmod(self.value*other.value,self.n),self.n)
    def __pow__(self, power, modulo=None):
        result=gmpy2.powmod(self.value,power,self.n)
        return rsaelement(result,self.n)
    def __str__(self):
        return "{0} % {1}".format(str(self.value),str(self.n))
bla = rsaelement()
print(bla)
print(bla**25876876)

poly=numpy.polynomial.polynomial.Polynomial([2,1,4,7])
print(poly)
print(poly(gmpy2.mpz(10)))