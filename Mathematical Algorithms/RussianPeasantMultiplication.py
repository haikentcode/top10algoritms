import sys
def russianPeasant(a,b):
    res = 0
    while b > 0:
        if b & 1 :
            res = res + a
        a = a << 1
        b = b >> 1
    return res

if __name__ == "__main__" :
   if len(sys.argv) > 2:
          a=int(sys.argv[1])
          b=int(sys.argv[1])
          print russianPeasant(a,b)
