import sys
def floorSqrt(x):
    if x == 0 || x == 1 :
        return x
    i = 1
    result = 1
    while result < x :
        if result == x :
            return result
        i=i+1
        result = i*i
    return i-1

def floorSqrtBinarySearch(x):
    if x == 0 || x == 1 :
        return x
    start = 1
    end = x
    ans=0
    while start <= end :
        mid = (start + end) / 2
        if mid*mid == x :
            return mid
        if mid*mid < x :
            start = mid + 1
            ans = mid
        else :
            end = mid - 1
    return ans

if __name__ == "__main__" :
      if len(sys.argv) > 1:
            x=int(sys.argv[1])
            print "O(n) Solution :"
            print floorSqrt(x)
            print "Solution By Binary Search :"
            print floorSqrtBinarySearch(x)
