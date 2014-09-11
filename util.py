import itertools

def is_prime(n):
   if (n%2 ==0): return False
   i = 3
   while i <= n**.5:
      if (n%i == 0): return False
      i += 2
   return True

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
  for file_number in range(1,41):
    with open('data/primes'+str(file_number)+'.txt') as f:
      for l in f:
        for j in (int(x) for x in l.split()):
           yield j            

def __calc_prime_divisors(n, x, duplicate=False):
    if (x*x > n) :
       if duplicate:
          s = list()
          s.append(n)
       else:
          s = set()
	  s.add(n)
       return s
    elif (n%x == 0):
       s =  __calc_prime_divisors(n/x, x, duplicate)
       if duplicate : s.append(x)
       else: s.add(x)
       return s
    else:
       return __calc_prime_divisors(n, x+(1 if x==2 else 2), duplicate) 

def get_prime_divisors(n,  duplicate=False):
    return __calc_prime_divisors(n, 2, duplicate) 

def get_max_prime_divisor(n):
    return max(get_prime_divisors(n))

def get_all_proper_divisors(n):
    s = set([1])
    prime_divisors = get_prime_divisors(n, duplicate=True)
    for num_factors in range(1,len(prime_divisors)):
        for combi in itertools.combinations(prime_divisors, num_factors):
            s.add(reduce(lambda x,y: x*y, combi))
    return s

def is_abundant(n):
    return sum(get_all_proper_divisors(n)) > n 

def get_abundant_numbers(n):
    return filter(is_abundant, range(12,n+1))

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

def bin_idx(lst, n, left, right):
    idx = (left + right) / 2
    if lst[idx] == n: return idx
    if left == right: return -1
    if lst[idx] < n:  return bin_idx(lst, n, idx+1, right)
    else: return bin_idx(lst, n, 0, idx-1)

class Fraction:
    def __init__(self, n, denominator=1):
        g = gcd(n, denominator)
        self.denominator = denominator/g
        self.numerator = n/g
    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator   = self.numerator * other.denominator + other.numerator * self.denominator
        g = gcd(new_denominator, new_numerator)
        return Fraction(new_numerator/g, new_denominator/g)
    def __mul__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator   = self.numerator * other.numerator
        g = gcd(new_denominator, new_numerator)
        return Fraction(new_numerator/g, new_denominator/g)
    def __div__(self, other):
        return self * Fraction(other.denominator, other.numerator)
    def __repr__(self):
        return "%d/%d" %(self.numerator, self.denominator)

