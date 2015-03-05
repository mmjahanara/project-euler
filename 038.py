import time

def euler038():
    for n1 in range(9876, 5677, -1):
        n2 = n1 + n1
        n1s = set(x for x in str(n1))
        n2s = set(x for x in str(n2))
        s = n1s.union(n2s)
        if len(s) == 9 and '0' not in s: return n1, n2
    return 0


if __name__ == '__main__' :
    a = time.time()
    print euler038()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
