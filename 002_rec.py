import time

def fib(a, b, c, s, end):
    if c > end: return s
    return fib(b+c, c+b+c, c+b+b+c+c, s+c, end)

def euler002():
    return fib(1, 1, 2, 0, 4000000)

if __name__ == '__main__' :
    a = time.time()
    print euler002()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
