from collections import defaultdict
numList=map(int,raw_input("Enter number present in array:").split())
def findMinRec(arr, i,sumCalculated,sumTotal):
    if i==0:
        return abs((sumTotal-sumCalculated) - sumCalculated)
    return min(findMinRec(arr, i-1, sumCalculated+arr[i-1], sumTotal),findMinRec(arr, i-1, sumCalculated, sumTotal))

def findMin(arr,n):
    sumTotal = 0
    for i in range(n):
        sumTotal = sumTotal + arr[i]
    return findMinRec(arr, n, 0, sumTotal);

def findMinDP(arr,n):
    sumTotal = 0;
    for i in range(n):
        sumTotal = sumTotal + arr[i]
    dp=[[0]*(sumTotal+1) for i in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = 1
    for i in range(1,sumTotal+1):
        dp[0][i] = 0;
    for i in range(n+1):
        for j in range(1,sumTotal+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j]|dp[i-1][j-arr[i-1]]
    diff = 1000000000
    j=sumTotal/2;
    while j>=0:
        if dp[n][j] == 1 :
            diff = sumTotal-2*j
            break
    return diff
print "Recursive Solution ",findMin(numList,len(numList))
print "Dynamic Solution ", findMinDP(numList,len(numList))
