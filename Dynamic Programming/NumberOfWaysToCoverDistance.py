def printCountRec(dist,n) :
    if dist<0:
        return 0
    if dist==0:
        return 1
    x=0
    for i in range(1,n+1):
        x=x+printCountRec(dist-i)
    return x

def printCountDP(int dist,n):
    count=[0]*(dist+1)
    count[0]  = 1,  count[1] = 1,  count[2] = 2
    for i in range(3,dist+1):
        for j in range(1,n+1):
            count[i]=count[i]+count[i-j]
    return count[dist]

if __name__ == "__main__" :
      if len(sys.argv) > 2:
            distance=int(sys.argv[1])
            maxnumberOfSteps=int(sys.argv[2])
            print "Recursive Solution: ",printCountRec(distance,maxnumberOfSteps)
            print "Recursive Solution: ",printCountDP(distance,maxnumberOfSteps)
