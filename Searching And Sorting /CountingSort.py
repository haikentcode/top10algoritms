from collections import defaultdict
nos=map(int,raw_input("Enter no for sort:").split())
def countingSort(array, mn, mx):
    count = defaultdict(int)
    for i in array:
        count[i] += 1
    result = []
    for j in range(mn,mx+1):
        result += [j]* count[j]
    return result
countingSort(nos,min(nos),max(nos))
print nos