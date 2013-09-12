import time
def euler107():
    num_v = 40
    edges = [dict() for _ in range(num_v)]

    filename = 'data/network.txt'
    with open(filename) as f:
        lines = f.readlines()
    for ln_number, ln in enumerate(lines):
        words = ln.split(',')
        for i,w in enumerate(words):
            try:
                edges[ln_number][i] = int(w)
            except:
                pass
    orig_weight = sum([sum(x[y] for y in x) for x in edges])/2

    all = set(range(0, num_v))
    x = {1}
    t = set()
    while len(x) < num_v:
        W = all - x
        v_from = min(x, key=lambda i: min(edges[i][y] for y in (W.intersection(edges[i]))) if len(W.intersection(edges[i])) != 0 else 999999)
        v_to   = min(W.intersection(edges[v_from]), key=lambda y: edges[v_from][y])
        print "from: %d, to: %d" % (v_from, v_to)
        x.add(v_to)
        t.add((v_from, v_to))
    return orig_weight - sum(edges[x[0]][x[1]] for x in t)


if __name__ == '__main__':
    a = time.time()
    print euler107()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
