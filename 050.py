import time
from util import prime, bin_idx

def euler050():
    m = 1000000
    pm = prime(m)
    x = [a for a in pm]
    max_l = 0
    for i in range(0, len(x)-1):
        s = x[i]
        for j in range(i+1, len(x)):
           s += x[j]
           if s > m: break
           if bin_idx(x, s, 0, len(x)-1) != -1: 
              if (max_l < j-i+1):
                 max_l = j-i+1
                 max_i, max_j = i,j
                 max_p = s
    print max_i, max_j
    return max_p
            
if __name__ == '__main__' :
    a = time.time()
    print euler050()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
