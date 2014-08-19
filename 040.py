import time
from util import prime, bin_idx

def euler040():
    n = 10000000
    s, i = '', 1
    while len(s) < n:
        s += str(i)
        i += 1
    arr = [1, 10, 100, 1000, 10000, 100000, 1000000]
    print reduce(lambda x,y: int(x)*int(y), list(s[x-1] for x in arr))

if __name__ == '__main__' :
    a = time.time()
    euler040()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
