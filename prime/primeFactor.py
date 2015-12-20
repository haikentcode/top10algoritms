import math
import sys
def primeFactor(n):
        while n%2==0:
            print 2,
            n/=2

        i=3
        while i*i < n :
            if n%i ==0:
                print i,
                n/=i
            i+=2
        if n>2 :
            print n,

if __name__=="__main__":
    if len(sys.argv) > 1:
        primeFactor(int(sys.argv[1]))
