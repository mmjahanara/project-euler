import time


def set_to_idx(s):
    return '_'.join(str(x) for x in sorted(s))


def idx_to_set(idx):
    arr = [int(x) for x in idx.split('_')]
    return set(arr)


def step(n):
    key = set_to_idx(set(range(0, 10)))
    s_all = 0
    a = [{} for i in range(0, 10)]
    for d in range(1, 10):
        a[d][set_to_idx(set([d]))] = 1
    for p in range(2, n+1):
        b = [{} for i in range(0, 10)]
        for d in range(0, 10):
            for left in (d-1, d+1):
                if left < 0 : continue
                if left > 9 : continue
                for idx in a[left]:
                    s = idx_to_set(idx)
                    s.add(d)
                    new_idx = set_to_idx(s)
                    if new_idx not in b[d]:
                        b[d][new_idx] = 0
                    b[d][new_idx] += a[left][idx]
        a = b
        s_all += sum(x[key] for x in b if key in x)
    return s_all


def euler178():
    return step(40)

if __name__ == '__main__' :
    a = time.time()
    print euler178()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
