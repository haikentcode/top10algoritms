class Node:
    """docstring for Node"""
    def __init__(self,key=26):
        self.data=[None]*key
        self.isword=False


class Trie:
    """simple trie by using list."""
    def __init__(self):
          self.head=None
    def insert(self,word):
          if self.head==None:
              self.head=Node()
          temNode=self.head
          for letter in word:
              key=lambda x:ord(x.lower())-ord('a')
              if not temNode.data[key(letter)]:
                  temNode.data[key(letter)]=Node()
              temNode=temNode.data[key(letter)]
          temNode.isword=True

    def find(self,word):
        temNode=self.head
        key=lambda x:ord(x.lower())-ord('a')
        if temNode:
            for letter in word:
                if temNode.data[key(letter)]:
                    temNode=temNode.data[key(letter)]
            if temNode.isword:
                return True
            else:
                return False
        else:
            return False




if  __name__=="__main__":
    a=Trie()
    a.insert("hitesh")
    a.insert("aditi")
    a.insert("gudan")
    print a.find("aditi")
    print a.find("haikent")
