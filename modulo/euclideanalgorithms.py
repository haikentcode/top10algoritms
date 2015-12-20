import sys


def gcd(a,b):
      if a==0:
          return b
      return gcd(b%a,a)


def agcdUtil(a,b,p):
    if a==0:
       p[0]=0
       p[1]=1
       return b
    ans=agcdUtil(b%a,a,p)
    x=p[1]-int(b/a)*p[0]
    y=p[0]
    p[0]=x
    p[1]=y
    return ans

def agcd(a,b):
      point=[0,0]
      return agcdUtil(a,b,point)


if __name__ == "__main__" :
   if len(sys.argv) > 2:
          a=int(sys.argv[1])
          b=int(sys.argv[2])
          print gcd(a,b),agcd(a,b)
