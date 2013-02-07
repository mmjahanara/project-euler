import time
import math

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

def euler020():
    return sum_of_digits(math.factorial(100))

def euler056():
    return max(sum_of_digits(pow(x,y)) for x in range(2,101) for y in range(1,101))

if __name__ == '__main__' :
    a = time.time()
    print euler020()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)

