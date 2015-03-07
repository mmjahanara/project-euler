import time

F = 0xF


def dict_to_idx(l):
    return '_'.join(str(x) for x in l)


def idx_to_dict(idx):
    words = idx.split('_')
    return [int(words[0]), int(words[1]), int(words[2])]


def init():
    n = {}
    for a in range (1, F+1):
        for b in range(0, F+1):
            for c in range(0, F+1):
                n0 = 1 if a == 0 or b == 0 or c == 0 else 0
                n1 = 1 if a == 1 or b == 1 or c == 1 else 0
                nF = 1 if a == F or b == F or c == F else 0
                if dict_to_idx([n0, n1, nF]) not in n:
                    n[dict_to_idx([n0, n1, nF])] = 0
                n[dict_to_idx([n0, n1, nF])] += 1
    return n


def num_words(n):
    x = init()
    s = x[dict_to_idx([1,1,1])]
    for i in range(4, n+1):
        y = {}
        y[dict_to_idx([0,0,0])] = x[dict_to_idx([0,0,0])] * 13
        y[dict_to_idx([0,0,1])] = x[dict_to_idx([0,0,1])] * 14 + x[dict_to_idx([0,0,0])]
        y[dict_to_idx([0,1,0])] = x[dict_to_idx([0,1,0])] * 14 + x[dict_to_idx([0,0,0])]
        y[dict_to_idx([1,0,0])] = x[dict_to_idx([1,0,0])] * 14 + x[dict_to_idx([0,0,0])]
        y[dict_to_idx([0,1,1])] = x[dict_to_idx([0,1,1])] * 15 + x[dict_to_idx([0,1,0])] + x[dict_to_idx([0,0,1])]
        y[dict_to_idx([1,0,1])] = x[dict_to_idx([1,0,1])] * 15 + x[dict_to_idx([1,0,0])] + x[dict_to_idx([0,0,1])]
        y[dict_to_idx([1,1,0])] = x[dict_to_idx([1,1,0])] * 15 + x[dict_to_idx([1,0,0])] + x[dict_to_idx([0,1,0])]
        y[dict_to_idx([1,1,1])] = x[dict_to_idx([1,1,1])] * 16 + x[dict_to_idx([1,1,0])] + x[dict_to_idx([0,1,1])] + x[dict_to_idx([1,0,1])]
        x = y
        s += x[dict_to_idx([1,1,1])]
    return s


def euler162():
    return num_words(16)

if __name__ == '__main__':
    a = time.time()
    print hex(euler162()).upper()[2:]
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
