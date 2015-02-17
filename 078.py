import time

N = 60000
w = [0] * (N+1)
w[0] = 1
coins = range(1, N+1)

def ways(target):
    for t in range(target, N+1):
        w[t] = w[t-target] + w[t]
    #return w[target]

def euler078():
    for n in range(1, N+1):
        if n % 100 == 0: print "n: %d" %n
        ways(n)
        x = w[n]
        #print x
        if x % 1000000 == 0:
            #print x
            return n

if __name__ == '__main__' :
    a = time.time()
    print euler078()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
