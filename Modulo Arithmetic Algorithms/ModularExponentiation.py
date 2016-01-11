import sys

def modExponentiation(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

if __name__ == "__main__" :
      if len(sys.argv) > 3:
            a=int(sys.argv[1])
            m=int(sys.argv[2])
            x=int(sys.argv[3])
            print modExponentiation(a,m,x)
