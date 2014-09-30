import time
from math import factorial as fact

def c(n,m):
    return fact(n)/fact(n-m)/fact(m)

def do_158(num_digits, num_chars):
    return c(num_chars, num_digits) * sum(c(num_digits-j, i-1) for i in range(1, num_digits) for j in range(1, num_digits-i+1))

def euler158():
    return max(do_158(i, 26) for i in range(1, 27))

if __name__ == '__main__':
    a = time.time()
    print euler158()
    print "time: %f millisec" % (1000 * (time.time() - a))
