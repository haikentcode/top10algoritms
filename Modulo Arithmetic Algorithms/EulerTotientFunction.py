import sys

"""

phi(n)=no of prime factor of n

"""
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def phi(n):
    result=0
    i=1
    while i < n:
        if gcd(i,n)==1:
            result+=1
        i+=1
    return result

def aphi(n):
    p=2
    result=n
    while p*p <= n:
          if n%p == 0:
                while n%p==0:
                    n/=p
                result*=(1.0-(1.0/float(p)))
          p+=1
    if n > 1:
        result*=(1.0-(1.0/float(n)))
    return int(result)


def aaphi(n):
     p=2
     result=n
     while p*p <= n :
         if n%p == 0:
             while n%p == 0:
                 n/=p
             result-=result/p
         p+=1
     if n >1:
        result-=result/n
     return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
         a=int(sys.argv[1])
         print "aaphi(a)",aaphi(a)
         print "aphi(a)",aphi(a)
         print "phi(a)",phi(a)
