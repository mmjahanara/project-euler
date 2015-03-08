import time
from util import lcm

def euler005():
    return reduce(lcm, range(1,21))

if __name__ == '__main__' :
    a = time.time()
    print euler005()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
