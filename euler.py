import time

def gcd(a,b):
    if (b == 0): return a
    while (a != b):
       if (a < b): a,b = b,a
       a = a-b 
    return a

# least common multiple
def lcm(a,b):
    return a*b/gcd(a,b)

def euler004():
    return max(filter(lambda x: str(x)==str(x)[::-1], (x*y for x in range(100,1000) for y in range(100, 1000)) ))

def euler005():
    return reduce(lcm, range(1,21))

def euler006():
    n = 100
    l = range(1,n+1)
    return sum(l)*sum(l)-sum(x*x for x in l)

if __name__ == '__main__' :
    a = time.time()
    print euler006()
    print "time elapsed: %f sec" % (time.time()-a)

