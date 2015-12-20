import sys

"""
a x= 1 (mod m)

"""

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)


def modInverse(a,m):
      i=2
      while i < m:
          if gcd(i,a)==1:
              return i
          i+=1      
      return -1


if __name__ == "__main__" :
      if len(sys.argv) > 2:
            a=int(sys.argv[1])
            m=int(sys.argv[2])
            print modInverse(a,m)
