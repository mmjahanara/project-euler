import time, math, decimal, itertools
from util import *

def euler002():
    a,b,c,sum = 1,1,2,0
    while (c <= 4000000):
      sum += c
      a = b+c
      b = c+a
      c = a+b
    return sum

def euler003():
    return get_max_prime_divisor(600851475143) 

def euler004():
    return max(filter(lambda x: str(x)==str(x)[::-1], (x*y for x in range(100,1000) for y in range(100, 1000)) ))

def euler005():
    return reduce(lcm, range(1,21))

def euler006():
    n = 100
    l = range(1,n+1)
    return sum(l)*sum(l)-sum(x*x for x in l)

def euler008():
    with open('data/008.txt') as f:
       s = ''.join([x.strip() for x in f.readlines()])
    return max([int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])*int(s[i+4]) for i in range(1,len(s)-4)])

def euler013():
    with open('data/13.txt', 'r') as f:
        lst = f.readlines()
    return str(reduce(lambda x,y: x+y, (int(x) for x in lst)))[:10]

def euler015():
    return math.factorial(40)/math.factorial(20)/math.factorial(20)
    
def euler016():
    return sum_of_digits(2**1000)

def euler018():
    return euler_018_067('18')

def euler_018_067(str_n):
    lst = []
    with open('data/'+str_n+'.txt') as f:
       for l in f.readlines():
           lst.append(map(int, l.split()))
    for x in range(1, len(lst)):
       lst[x][0] = lst[x-1][0]+lst[x][0]
       for y in range(1, len(lst[x])-1):
           lst[x][y] = max(lst[x-1][y-1], lst[x-1][y])+lst[x][y]
       y = len(lst[x])-1
       lst[x][y] = lst[x-1][y-1]+lst[x][y]
    return max(lst[len(lst)-1])

def euler020():
    return sum_of_digits(math.factorial(100))
    
def euler021():
    s = set()
    for n in range(1,10000):
        x = sum(get_all_proper_divisors(n))
        y = sum(get_all_proper_divisors(x))
        if n != x and n == y: s.add(n)
    return sum(s)

def euler023():
    s = set()
    for combi in itertools.combinations_with_replacement(get_abundant_numbers(28123), 2):
        s.add(combi[0]+combi[1])
    t = set(range(1,28124))
    return sum(t.difference(s))

def euler029():
    return len(set(a**b for a in range(2,101) for b in range(2,101)))

def euler030():
    return sum(x for x in range(2, 400000) if x == sum(int(y)**5 for y in str(x)))

def euler037():
    # https://en.wikipedia.org/wiki/List_of_prime_numbers#Two-sided_primes
    two_sided_primes = '23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397'
    return sum(int(x) for x in two_sided_primes.split(','))

def euler047():
    i = 100
    while(len(get_prime_divisors(i))!=4 or len(get_prime_divisors(i+1))!=4 or len(get_prime_divisors(i+2))!=4 or len(get_prime_divisors(i+3))!=4):
        i += 1
    return i

def euler048():
    return str(sum(map(lambda x: x**x, range(1,1001))))[-10:]

def euler056():
    return max(sum_of_digits(pow(x,y)) for x in range(2,101) for y in range(1,101))

def euler058():
    nums = [3,5,7,9]
    inc  = [10,12,14,16]
    count_prime = 3 
    count_num = 5
    size = 3
    t = 7
    idx = 0
    while 10*count_prime >= count_num:
        idx += 1
        nums = [x+y for x,y in zip(nums, inc)]
        inc  = [x+8 for x in inc]
        count_num += 4
        size += 2
        for x in nums:
           if is_prime(x): count_prime += 1
    print size

def euler067():
    return euler_018_067('67')

def euler080():
    decimal.getcontext().prec=102
    s = 0
    for i in range(2,101):
        if i in [4,9,16,25,36,49,64,81,100]: continue
        t = str(decimal.Decimal(i).sqrt())
        dec = t[2:101]
        s += sum(int(x) for x in dec)+ int(math.sqrt(i)) 
    return s

def euler120():
    return sum(max((2*n*a)%(a*a) for n in range(1,a)) for a in range(3,1001))
        
if __name__ == '__main__' :
    a = time.time()
    print euler047()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)

