import time

def get_num_plans(num_blocks, min_size = 3):
    a = [0] * (num_blocks + 1)
    for i in range(min_size, num_blocks+1):
        a[i] = a[i-1] + sum((a[i-x-1]+1) for x in range(min_size, i)) + 1
    return a[-1] + 1

def euler114():
    return get_num_plans(50, 3)

if __name__ == '__main__':
    a = time.time()
    print euler114()
    print "time: %f millisec" % (1000 * (time.time() - a))