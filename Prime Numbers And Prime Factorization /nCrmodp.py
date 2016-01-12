import math
import sys
def nCrModp(n, r, p):
    C=[0]*(r+1)
    C[0]=1
    i=1
    while i<=n :
        j=min(i,r)
        while j>0 :
            C[j] = (C[j] + C[j-1])%p
            j=j-1
        i=i+1
    return C[r]
if __name__=="__main__":
    if len(sys.argv) > 3:
        print nCrModp(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
