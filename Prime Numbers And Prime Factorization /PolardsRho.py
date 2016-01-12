from random import randint
from fractions import gcd
from math import *

def PollardRho(n):
    i=0;
    xi=randint(0,n-1);
    k=2
    y=xi
    while i< n:
        i=i+1
        xi=((xi^2)-1)%n
        d=gcd(y-xi,n)
        if d!=1 and d!=n:
            print d;
        if i==k:
            y=xi
            k=2*k
if __name__=="__main__":
    if len(sys.argv) > 1:
        PollardRho(int(sys.argv[1]))
