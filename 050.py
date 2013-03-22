import time

# calculates prime numbers not greater than m.
# note that m must be at least 5
def prime(m = 100):
    yield 2
    yield 3
    size = (m-2)/3 # 6k+1, and 6k-1
    if m%6 == 1: size += 1
    lst = [True] * size
    i = 0
    while i < len(lst):
       if lst[i]:
          k   = i/2+1
          num = 6*k-1 if (i%2==0) else 6*k+1
          x = num+num
          while (x <= m):
             res = x%6
             if res == 1:
                lst[(x-2)/6*2+1]= False
             elif res == 5:
                lst[(x-2)/6*2] = False
             x += num
          yield num
       i += 1

def euler050():
    m = 1000000
    pm = prime(m)
    x = [a for a in pm]
    max_l = 0
    for i in range(0, len(x)-1):
        s = x[i]
        for j in range(i+1, len(x)):
           s += x[j]
           if s > m: break
           if bin_idx(x, s, 0, len(x)-1) != -1: 
              if (max_l < j-i+1):
                 max_l = j-i+1
                 max_i, max_j = i,j
                 max_p = s
    print max_i, max_j
    return max_p
            
def bin_idx(lst, n, left, right):
    idx = (left + right) / 2
    if lst[idx] == n: return idx
    if left == right: return -1
    if lst[idx] < n:  return bin_idx(lst, n, idx+1, right)
    else: return bin_idx(lst, n, 0, idx-1)

if __name__ == '__main__' :
    a = time.time()
    print euler050()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
