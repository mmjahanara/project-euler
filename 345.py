import time
import sys
import itertools
import random

def simulate(a):
    rg = range(len(a))
    old_sum = 0
    over_all_idx = []
    for outer in range(100):
        random.shuffle(rg)
        indices = rg[:]
        sum_one_round = 0
        for _ in range(50000):
            pair = random.choice(list(itertools.combinations(rg, 2)))
            x,y = pair[0], pair[1]
            new_idx = indices[:]
            new_idx[x], new_idx[y] = new_idx[y], new_idx[x]
            new_sum = sum(a[i][new_idx[i]] for i in rg)
            if sum_one_round < new_sum:
                indices = new_idx
                sum_one_round = new_sum
        if old_sum < sum_one_round:
            old_sum = sum_one_round
            over_all_idx = indices
        print outer, old_sum
    return over_all_idx


def euler345(f_name):
    a = []
    with open(f_name) as f:
        for line in f:
            x = [int(w) for w in line.split()]
            a.append(x)

    rg = range(len(a))
    indices = simulate(a)
    print indices
    return sum(a[i][indices[i]] for i in rg)

if __name__ == '__main__' :
    a = time.time()
    f_name = 'data/345.txt'
    if len(sys.argv) > 1: f_name = sys.argv[1]
    print euler345(f_name)
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
