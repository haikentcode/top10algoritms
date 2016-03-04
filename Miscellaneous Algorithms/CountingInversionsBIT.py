from collections import defaultdict
numList=map(int,raw_input("Enter number present in array:").split())

def getSum(BITree,index):
    sum = 0
    while index > 0:
        sum = sum + BITree[index]
        index = index - index & (-index)
    return sum

def updateBIT(BITree,n,index,val):
    while index <= n:
        BITree[index] =BITree[index]+ val
        index = index+index & (-index)

def getInvCount(arr,n):
    invcount = 0
    maxElement = 0;
    for i in range(n):
        if maxElement < arr[i]:
            maxElement = arr[i]
    BIT[maxElement+1];
    for i in range(1,maxElement+1):
        BIT[i] = 0
    i=n-1
    while i>=0:
        invcount = invcount + getSum(BIT, arr[i]-1)
        updateBIT(BIT, maxElement, arr[i], 1)
        i=i-1
    return invcount

def convert(arr,n):
    temp=[0]*n;
    for i in range(n):
        temp[i] = arr[i]
    temp.sort();
    for i in range(n):
        arr[i] = temp.index(arr[i])+1

def getInvCountAdvance(arr,n):
    invcount = 0
    convert(arr, n)
    BIT=[0]*(n+1);
    for i in range(n+1):
        BIT[i] = 0;
    i=n-1
    while i>=0:
        invcount = invcount+getSum(BIT, arr[i]-1)
        updateBIT(BIT, n, arr[i], 1)
        i=i-1
    return invcount

print "Navie Bit solution"
print getInvCount(numList,len(numList))
print "Θ(n) solution solution"
print getInvCountAdvance(numList,len(numList))
