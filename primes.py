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

def __calc_prime_divisors(n, x):
    if (x*x > n) :
       s = set()
       s.add(n)
       return s
    elif (n%x == 0):
       s =  __calc_prime_divisors(n/x, x)
       s.add(x)
       return s
    else:
       return __calc_prime_divisors(n, x+(1 if x==2 else 2)) 

def get_prime_divisors(n):
    return __calc_prime_divisors(n, 2) 

def get_max_prime_divisor(n):
    return max(get_prime_divisors(n))

