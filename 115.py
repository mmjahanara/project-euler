import time

def get_num_plans(num_blocks, min_size = 3):
    a = [0] * (num_blocks + 1)
    for i in range(min_size, num_blocks+1):
        a[i] = a[i-1] + sum((a[i-x-1]+1) for x in range(min_size, i)) + 1
    return a[-1] + 1

def do_115(m, threshold):
    n = m + 1
    x = get_num_plans(n, m)
    while x < threshold:
        n += 1
        x = get_num_plans(n, m)
    return n

def euler115():
    return do_115(50, 1000000)

if __name__ == '__main__':
    a = time.time()
    print euler115()
    print "time: %f millisec" % (1000 * (time.time() - a))