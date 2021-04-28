#a^e mod n
from Crypto.Util.number import *
import gmpy2
from math import log,ceil
a=2
e=123
n=35
print(bin(e))
ex=a
lastx=a
for i in range(ceil(log(e,2))):
    print("x{0}={1}".format(i,lastx))
    lastx=pow(lastx,2,n)

    if(e&(1<<i+1)):
        ex*=lastx
print(pow(ex,1,n))