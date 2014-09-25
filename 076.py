import time

def num_summation(n):
    a = [[0] * (n/2)]
    for idx in range(2, n+1):
        a.append([1+sum(a[idx-y-2][j] for j in range(y, len(a[idx-y-2]))) for y in range(idx/2)])
    return sum(a[-1])

def euler076():
    return num_summation(100)

if __name__ == '__main__':
    a = time.time()
    print euler076()
    print "time elapsed: %f millisec" % ((time.time()-a) * 1000)

