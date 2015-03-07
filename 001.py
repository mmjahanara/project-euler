import time

def euler001():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1001)))

if __name__ == '__main__' :
    a = time.time()
    print euler001()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
