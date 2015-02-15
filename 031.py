import time

def ways(target, coins):
    w = [0] * (target+1)
    w[0] = 1
    for c in coins:
        for t in range(c, target+1):
            w[t] = w[t-c] + w[t]
    return w[target]

def euler031():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return ways(500, coins)

if __name__ == '__main__' :
    a = time.time()
    print euler031()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
