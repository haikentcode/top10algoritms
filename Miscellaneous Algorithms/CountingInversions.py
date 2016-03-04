from collections import defaultdict
numList=map(int,raw_input("Enter number present in array:").split())

count = 0
def getInvCount(arr,n):
    inv_count = 0
    for i in range(n):
        for i in range(i+1,n):
            if arr[i]>arr[j] :
                inv_coun=inv_count+1
    return inv_count

def inversionsCount(x):
    global count
    midsection = len(x) / 2
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:
        # Divid and conquer with recursive calls
        # to left and right arrays similar to
        # merge sort algorithm
        inversionsCount(leftArray)
        inversionsCount(rightArray)

        # Merge sorted sub-arrays and keep
        # count of split inversions
        i, j = 0, 0
        a = leftArray; b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k +=1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k+= 1
                        x[k] = a[i]
                        i += 1
                    break
    return x
print "Logrithmic solution"
inversionsCount(numList)
print count
print "nsaquare solution solution"
print getInvCount(numList,len(numList))
