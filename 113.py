import time
import itertools as it
import sys
import copy
import math

def test_is_bouncy():
    assert not is_bouncy(135)
    assert not is_bouncy(200)
    assert is_bouncy(185)
    assert is_bouncy(523)
    assert is_bouncy(151)
    assert not is_bouncy(66420)
    assert is_bouncy(277032)

def is_bouncy(n):
    zero, plus, minus = False, False, False
    s = str(n)
    for i in range(0, len(s)-1):
        d = int(s[i+1])-int(s[i]) 
        if   d < 0 : minus = True
        elif d > 0 : plus  = True
        else: zero = True
    return (plus and minus)

# param l: length (num of digits) of the number
def num_not_bouncy_numbers_first_last_length(a,e,l):
    d = abs(e-a)
    return math.factorial(d+l-2)/math.factorial(l-2)/math.factorial(d)

def e113():
    return sum(num_not_bouncy_numbers_first_last_length(a,e,l) for a in range(1,10) for e in range(0,10) for l in range(2,101)) + 9

def test_not_bouncy_numbers_first_last_length():
    s = 0
    for i in range(1000, 10000):
       if str(i)[0] != '9' or str(i)[-1] != '5': continue
       if not is_bouncy(i): s += 1
    print s
    assert s == num_not_bouncy_numbers_first_last_length(9,5,4)
       
        
if __name__ == '__main__':
    #test_is_bouncy()
    #test_not_bouncy_numbers_first_last_length()
    a = time.time()
    print e113()
    print "%f sec" % (time.time()-a)

