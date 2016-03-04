import sys
def catalan(n):
    if n <=1 :
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
    return res
if __name__ == "__main__" :
   if len(sys.argv) > 1:
          a=int(sys.argv[1])
          print catalan(a)
