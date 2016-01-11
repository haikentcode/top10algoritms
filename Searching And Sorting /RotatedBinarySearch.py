nos=map(int,raw_input("Enter nos: ").split())
key=input("Enter key to search: ")

def pivot(lst,l,r):
      if l>r:
        return -1
      if l==r:
         return l
      mid=(l+r)/2

      if mid < r and lst[mid]>lst[mid+1]:
               return mid
      if  mid > l and lst[mid] < lst[mid-1]:
               return mid-1
      if lst[l] >= lst[mid]:
              return pivot(lst,l,mid-1)
      return pivot(lst,mid+1,r)


def findPivot(lista):
       return pivot(lista,0,len(lista))

def rbsearch(lst,l,r,k):
       mid=(l+r)/2
       if l > r:
          return -1
       if lst[mid]==k:
             return mid
       if lst[l]<=lst[mid]:
            if k >= lst[l] and k <= lst[mid]:
                   return rbsearch(lst,l,mid-1,k)
            return rbsearch(lst,mid+1,r,k)
       if k >=lst[mid] and k <= lst[r]: 
                    return rbsearch(lst,mid+1,r,k)
       return rbsearch(lst,l,mid-1,k)


print findPivot(nos)
print rbsearch(nos,0,len(nos)-1,key)
