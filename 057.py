import time
from util import Fraction

def do_057(num):
    s = 0
    seed = Fraction(1,2)
    for _ in range(2, num+1):
        seed = Fraction(1)/(Fraction(2)+seed)
        frac = Fraction(1) + seed
        if len(str(frac.numerator)) > len(str(frac.denominator)): s += 1
    return s


def euler057():
    return do_057(1000)

if __name__ == '__main__':
    a = time.time()
    print euler057()
    print "time: %f millisec" % (1000 * (time.time() - a))