import sys

"""
a x= 1 (mod m)

"""




def modInverse(a,m):
      i=2
      while i < m:
          if (a*i)%m ==1:
              return i
          i+=1
      return -1


def gcdExtend(a,b,p):
    if a==0:
       p[0]=0
       p[1]=1
       return b
    ans=gcdExtend(b%a,a,p)
    x=p[1]-int(b/a)*p[0]
    y=p[0]
    p[0]=x
    p[1]=y
    return ans

def amodInv(a,m):
    p=[0,0]
    g=gcdExtend(a,m,p)
    if not g == 1:
       print "provided numbers are not coprime"
    else:
       res=(p[0]%m+m)%m
       return res



if __name__ == "__main__" :
      if len(sys.argv) > 2:
            a=int(sys.argv[1])
            m=int(sys.argv[2])
            print modInverse(a,m)
            print amodInv(a,m)
