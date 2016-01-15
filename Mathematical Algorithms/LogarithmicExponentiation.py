import sys
def power(x,y):
    if y == 0 :
        return 1;
    elif y%2 == 0 :
        return power(x, y/2)*power(x, y/2)
    else :
        return x*power(x, y/2)*power(x, y/2)

if __name__ == "__main__" :
      if len(sys.argv) > 2:
            a=int(sys.argv[1])
            m=int(sys.argv[2])
            print power(a,m)
