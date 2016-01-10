import sys

def findMinX(n,r):
    x=1
    while True:
        j=0
        while j < len(n):
            if not x%n[j]==r[j]:
                break
            j+=1
        if j==len(n):
           return x
        x+=1

def minv(a,m):
      i=2
      while i < m:
          if (a*i)%m ==1:
              return i
          i+=1
      return -1

def crtheorem(n,r):
       prod=1
       for x in n:
           prod*=x
       pp=[]
       inv=[]
       for a in n:
            pp.append(prod/a)

       i=0
       while  i< len(n):
           inv.append(minv(pp[i],n[i]))
           i+=1
       x=sum([x*y*z for x,y,z in zip(r,pp,inv)])
       return x%prod


if __name__== "__main__":
     n=[3, 4, 5]
     r=[2, 3, 1]
     print findMinX(n,r),crtheorem(n,r)
