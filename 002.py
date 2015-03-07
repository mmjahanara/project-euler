import time

def euler002():
    a, b, c, s= 1, 1, 2, 0
    while (c <= 4000000):
      s += c
      a = b+c
      b = c+a
      c = a+b
    return s

if __name__ == '__main__' :
    a = time.time()
    print euler002()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
