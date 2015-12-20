import math
import sys
import random
def log2(n):
    return math.log(n)/math.log(2)


def power(x,y,p):
    '(x^y)%p'
    res=1
    x=x%p
    while y:
        if y & 1:
            res=(res*x)%p
        x=(x*x)%p
        y=y>>1
    return res

class primalityTest:
          """
          1.O(n)
          2.O(n^1/2)
          3.Fermat O(k Log n)
          4.Miller-Rabin Miller-Rabin
          """
          def __init__(self):
               pass

          def isPrime(self,n,test=1):
               if test==1 :
                   return self.isPrimeTest1(n)
               elif test==2:
                   return self.isPrimeTest2(n)
               elif test==3:
                     return self.isPrimeTest3(n)
               elif test==4:
                   return self.isPrimeTest4(n)
               else:
                    print "out of range method index"

          def isPrimeTest1(self,n):
                i=2
                while i < n-1 :
                       if n%i==0:
                            return False
                       i+=1
                return True

          def isPrimeTest2(self,n):
                   if n <=1 :
                       return False
                   if  n <=3 :
                       return True

                   if n%2==0 or n%3==0 :
                        return False

                   i=5
                   while i*i < n :
                       if n%i==0  or n%(i+2)==0:
                              return False
                       i+=6
                   return True
          def isPrimeTest3(self,n):
              '''Fermat Method'''
              if n <=1 or n==4 :
                  return False
              if n <= 3 :
                   return True
              maxk=int(math.ceil(log2(n)))
              k=maxk
              while k :
                  a=random.randint(2,n-1)
                  if not power(a,n-1,n)==1:
                       return False
                  k-=1
              return True
              
          def millerRabinTest(self,n,d):
                   a=random.randint(2,n-1)
                   x=power(a,d,n) # (a^d)%n
                   if x==1 or x==n-1 :
                        return True
                   while  not d==n-1:
                       x=(x*x)%n
                       d*=2
                       if x==1:
                           return False
                       if x==n-1:
                           return True
                   return False

          def isPrimeTest4(self,n):
             'Miller-Rabin Method'
             d=n-1
             while  d%2==0:
                 d /=2
             k=5
             if n<=1 or n==4 :
                 return False
             if n <= 3 :
                 return True

             while k :
                 if self.millerRabinTest(n,d)==False :
                        return False
                 k-=1
             return True


if __name__=="__main__":
        if len(sys.argv) > 1:
              n=int(sys.argv[1])
              if len(sys.argv) > 2 :
                  t=int(sys.argv[2])
              else:
                  t=1
              pt=primalityTest()
              r=pt.isPrime(n,t)
              print r
