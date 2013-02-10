import time
import math

# calculates prime numbers not greater than m.
# note that m must be at least 5
def prime(m = 100):
    yield 2
    yield 3
    size = (m-2)/3 # 6k+1, and 6k-1
    if m%6 == 1: size += 1
    lst = [True] * size
    i = 0
    while i < len(lst):
       if lst[i]:
          k   = i/2+1
          num = 6*k-1 if (i%2==0) else 6*k+1
          x = num+num
          while (x <= m):
             res = x%6
             if res == 1:
                lst[(x-2)/6*2+1]= False
             elif res == 5:
                lst[(x-2)/6*2] = False
             x += num
          yield num
       i += 1

def prime_iterator():
  with open('data/primes1.txt') as f:
    for l in f:
      for j in (int(x) for x in l.split()):
         yield j            

def gcd(a,b):
    if (b == 0): return a
    while (a != b):
       if (a < b): a,b = b,a
       a = a-b 
    return a

# least common multiple
def lcm(a,b):
    return a*b/gcd(a,b)

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

def euler002():
    a,b,c,sum = 1,1,2,0
    while (c <= 4000000):
      sum += c
      a = b+c
      b = c+a
      c = a+b
    return sum

def euler004():
    return max(filter(lambda x: str(x)==str(x)[::-1], (x*y for x in range(100,1000) for y in range(100, 1000)) ))

def euler005():
    return reduce(lcm, range(1,21))

def euler006():
    n = 100
    l = range(1,n+1)
    return sum(l)*sum(l)-sum(x*x for x in l)

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

def euler030():
    return sum(x for x in range(2, 400000) if x == sum(int(y)**5 for y in str(x)))

def euler037():
    # https://en.wikipedia.org/wiki/List_of_prime_numbers#Two-sided_primes
    two_sided_primes = '23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397'
    return sum(int(x) for x in two_sided_primes.split(','))

def euler056():
    return max(sum_of_digits(pow(x,y)) for x in range(2,101) for y in range(1,101))

def euler058():
    primes = prime(50000000)
    l = (set(primes))
    nums = [3,5,7,9]
    inc  = [10,12,14,16]
    count_prime = 3 
    count_num = 5
    size = 3
    while 10*count_prime >= count_num:
        nums = [x+y for x,y in zip(nums, inc)]
        inc  = [x+8 for x in inc]
        count_num += 4
        size += 2
        count_prime += len(set(nums).intersection(l))
        print "size: %d, nums: %s, count_prime: %d, count_num: %d, ratio: %f" % (size, nums, count_prime, count_num, count_prime/(count_num+0.0))
    print size

def euler067():
    return euler_018_067('67')

if __name__ == '__main__' :
    a = time.time()
    print euler058()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)

