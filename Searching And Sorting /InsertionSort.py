nos=map(int,raw_input("Enter no for sort: ").split())


def sort(a):
      n=len(a)
      i=1
      while i<n:
            key=a[i]
            j=i-1
            while j >=0 and a[j]>key:
                     a[j+1]=a[j]
                     j-=1
            a[j+1]=key
            i+=1


sort(nos)
print nos
