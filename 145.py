import time

def euler145():
    n2 = no_carry_odd_no_0()
    n3 = no_carry_odd_no_0() * len([0,1,2,3,4])
    n4 = no_carry_odd_no_0() * no_carry_odd_with_0()
    n6 = n4 * no_carry_odd_with_0()
    n7 = (carry_odd_no_0() * no_carry_even_with_0()) * (len([0,1,2,3,4]) * carry_odd_with_0())
    n8 = n4 * (no_carry_odd_with_0() * no_carry_odd_with_0())
    return n2 + n3 + n4 + n6 + n7 + n8

def no_carry_odd_with_0():
    return 30;

def no_carry_even_with_0():
    return 25;

def no_carry_odd_no_0():
    return 20

def carry_odd_with_0():
    return 20

def carry_odd_no_0():
    return 20

def carry_even_with_0():
    return 25

if __name__ == '__main__':
    a = time.time()
    print euler145()
    print "time elapsed: %f millisec" % (1000*(time.time()-a))
