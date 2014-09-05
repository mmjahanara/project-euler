import time

def get_num_plans(num_blocks, colors):
    s = 0
    for size in colors:
        a = [0] * (num_blocks + 1)
        for i in range(size, num_blocks+1):
            a[i] = a[i-1] + a[i-size] + 1
        s += a[-1]
    return s

def euler116():
    return get_num_plans(50, [2,3,4])

if __name__ == '__main__':
    a = time.time()
    print euler116()
    print "time: %f millisec" % (1000 * (time.time() - a))