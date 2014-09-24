import time
from util import Fraction

def digit(idx):
    return 1 if idx % 3 != 2 else 2 * ((idx-2)/3 + 1)

def e(n):
    current = digit(n)
    for idx in xrange(n-1, 0, -1):
        dgt = digit(idx)
        current = Fraction(dgt) + Fraction(1) / current
    return Fraction(2) + Fraction(1)/current

def euler065():
    e99 = e(99)
    print sum(int(x) for x in str(e99.numerator))

if __name__ == '__main__':
    a = time.time()
    euler065()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
