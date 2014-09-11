import time

def get_num_plans(num_blocks, colors):
    a = [0, 0, 1, 3, 7] # a[0] is only a place holder!
    for l in range(5, num_blocks+1):
        a.append(a[l-1] + sum(a[l-i] + 1 for i in colors))
    return a[num_blocks] + 1

def euler117():
    return get_num_plans(50, [2,3,4])

if __name__ == '__main__':
    a = time.time()
    print euler117()
    print "time: %f millisec" % (1000 * (time.time() - a))