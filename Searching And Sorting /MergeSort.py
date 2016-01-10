nos=map(int,raw_input("Enter no's for sort: ").split())


def merge(a,l,m,r):
      L=a[l:m+1]
      R=a[m+1:r+1]
      i=0
      j=0
      k=l
      while i<len(L) and j<len(R):
             if L[i]<=R[j]:
                 a[k]=L[i]
                 i+=1
             else:
                 a[k]=R[j]
                 j+=1
             k+=1
      while i < len(L):
              a[k]=L[i]
              k+=1
              i+=1
      while j < len(R):
              a[k]=R[j]
              j+=1
              k+=1

      

def mergeSort(a,l,r):
   if l<r:
      mid=(l+r)/2
      mergeSort(a,l,mid)
      mergeSort(a,mid+1,r)
      merge(a,l,mid,r)



def sort(a):
      mergeSort(a,0,len(a)-1)

sort(nos)
print nos
