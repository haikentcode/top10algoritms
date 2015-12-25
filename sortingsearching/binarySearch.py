nos=map(int,raw_input("Enter nos: ").split())
key=input("searching key: ")


def bsearch(lst,left,right,key):
       if left<right:
             mid=(left+right)/2
             if lst[mid]==key:
                    return True
             elif lst[mid]<key:
                   return bsearch(lst,mid+1,right,key)
             else:
                   return bsearch(lst,left,mid-1,key)
       return False


def search(lista,key):
       return bsearch(lista,0,len(lista),key)

print search(nos,key)
 
