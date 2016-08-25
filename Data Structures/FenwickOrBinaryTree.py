class Bit:
      def __init__(self,a):
           self.a = a
           self.n = len(a)
           self.bit = [0]*(self.n+1)
           for i,x in enumerate(a):
                     if i == 0 : continue
                     self.update(i,x)

      def update(self,x,val):
              while x <= self.n:
                   self.bit[x] += val
                   x += x&-x

      def query(self,x):
             sum=0
             while x > 0:
                  sum +=self.bit[x]
                  x -=x&-x
             return sum




if __name__ == "__main__":
             a=[1,23,3,4,4,4,4,4,4,5,5]
             bt = Bit(a)
             print "query(4)", bt.query(4)
             print "update(2,6)"
             bt.update(2,6)
             print "query(4)",bt.query(4)
