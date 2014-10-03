import time

def do_191(n):
    # x_y: x: num of Ls, y: num of continuous As and the end
    a = {}
    a['0_0'] = 2
    a['0_1'] = 1
    a['0_2'] = 1
    a['1_0'] = 3
    a['1_1'] = 1
    a['1_2'] = 0
    #a['2_0'] = 1
    #a['2_1'] = 0
    #a['2_2'] = 0
    for _ in xrange(3, n+1):
        b = {}
        b['0_0'] = a['0_0'] + a['0_1'] + a['0_2']
        b['0_1'] = a['0_0']
        b['0_2'] = a['0_1']
        b['1_0'] = a['0_0'] + a['0_1'] + a['0_2'] + a['1_0'] + a['1_1'] + a['1_2']
        b['1_1'] = a['1_0']
        b['1_2'] = a['1_1']
        a = b
    return sum(b[x] for x in b)

def euler191():
    return do_191(30)

if __name__ == '__main__':
    a = time.time()
    print euler191()
    print "time elapsed: %f millisec" % ((time.time()-a) * 1000)

