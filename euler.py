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
    print max(filter(lambda x: str(x)==str(x)[::-1], (x*y for x in range(100,1000) for y in range(100, 1000)) ))

def euler005():
    print reduce(lcm, range(1,21))

if __name__ == '__main__' :
    a = time.time()
    euler005()
    print "time elapsed: %f sec" % (time.time()-a)

