import time

SIZE = 9

def _slow_no_digit_more_than_x_times(max_repetition, num_digit):
    a = dict()
    for i in range(1, SIZE+1):
        key = tuple([1 if j==i else 0 for j in range(SIZE+1)])
        a[key] = 1
    for d in range(2, num_digit+1):
        b = dict()
        for key, value in a.items():
            for n in range(SIZE+1):
                occurrence = key[n]
                if occurrence < max_repetition:
                    new_key = tuple([key[x] if x != n else occurrence+1 for x in range(SIZE+1)])
                    if not new_key in b:
                        b[new_key] = 0
                    b[new_key] += value
        a = b
    return sum(a[x] for x in a)

def euler172():
    return _slow_no_digit_more_than_x_times(3, 18)

if __name__ == '__main__':
    a = time.time()
    print euler172()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
