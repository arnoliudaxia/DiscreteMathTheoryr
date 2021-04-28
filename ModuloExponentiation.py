#a^e mod n
from math import log,ceil
import basicAlogrism

def powerfulPower(a,e,n):
    #print(bin(e))
    ex=a
    lastx=a
    for i in range(ceil(log(e,2))):
        #print("x{0}={1}".format(i,lastx))
        lastx=((lastx*lastx)%n)

        if(e&(1<<i+1)):
            ex*=lastx
    return ex%n