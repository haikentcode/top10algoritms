nolist=map(int,raw_input("Enter nos: ").split())
key=input("Search key: ")

def search(lista,key):
      for x in lista:
            if x==key:
                return True
      return False

print search(nolist,key)
