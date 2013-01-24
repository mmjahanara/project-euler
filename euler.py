from time import time

def euler004():
    print max(filter(lambda x: str(x)==str(x)[::-1], (x*y for x in range(100,1000) for y in range(100, 1000)) ))


if __name__ == '__main__' :
    a = time()
    euler004()
    print "time elapsed: %f millisec" % (time()-a)

