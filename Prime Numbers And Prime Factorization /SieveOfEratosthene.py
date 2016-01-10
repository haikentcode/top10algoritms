import math
import sys
class primRange:
    def __init__(self):
         pass

    def eratosthenes(self,n):
          p=[True]*(n+1)
          p[0]=False
          p[1]=False
          for i in range(2,n):
              if p[i] :
                  print i," ",
                  for j in range(i,n,i):

                       p[j]=False

if  __name__=="__main__":
      if len(sys.argv) > 1 :
            n=int(sys.argv[1])
            pr=primRange()
            pr.eratosthenes(n)
