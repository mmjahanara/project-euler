import time

def euler008():
    n = 13
    with open('data/008.txt') as f:
       s = [int(x) for x in ''.join([x.strip() for x in f.readlines()])]
    return max((reduce(lambda x, y: x*y, s[i:i+n]) for i in range(0, len(s)-n)))

if __name__ == '__main__' :
    a = time.time()
    print euler008()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
