nos=map(int,raw_input("Enter no for sort:").split())


def sort(lst):
      n=len(lst)
      i=0
      while i<n:
           j=0
           hk=False
           while j<n-i-1:
                 if lst[j]>lst[j+1]:
                       tm=lst[j]
                       lst[j]=lst[j+1]
                       lst[j+1]=tm
                       hk=True
                 j+=1
           if not hk:
               break
           i+=1



sort(nos)
print nos
