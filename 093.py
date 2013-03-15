import time
import itertools as it
import sys

def print_expr(a):
    stk = []
    for x in a:
      if x in ['+','-','*','/']:
         a1,a2 = stk.pop(), stk.pop()
         t = '('+str(a1)+x+str(a2)+')'
         stk.append(t)
      else: stk.append(x)
    return stk[0]

def eval_expr(a):
    stk = []
    for x in a:
      if x in ['+','-','*','/']:
         a1,a2 = float(stk.pop()), float(stk.pop())
         t = a1+a2 if x=='+' else a1-a2 if x=='-' else a1*a2 if x=='*' else float(a1)/a2
         stk.append(t)
      else: stk.append(x)
    return stk[0]

def has_solution(nu, x):
    for nu_p in it.permutations(nu):
      for op_p in it.product('+-*/', repeat=3):
        t = list(nu_p)
        q = list(op_p)
        a1 = [t[0],t[1],q[0],t[2],t[3],q[1],q[2]]
        a2 = [t[0],t[1],q[0],t[2],q[1],t[3],q[2]]
        a3 = [t[0],t[1],t[2],q[0],q[1],t[3],q[2]]
        a4 = [t[0],t[1],t[2],t[3],q[0],q[1],q[2]]
        try:
          if eval_expr(a1) == x: 
             return True
          if eval_expr(a2) == x: 
             return True
          if eval_expr(a3) == x:
             return True
          if eval_expr(a4) == x: 
             return True
        except :
          pass
    return False

def euler093():
    max = 0
    for n in it.combinations(range(1,10), 4):
        nu = list(n)
        x = 1
        while has_solution(nu, x):
          x += 1
        if max < x-1: 
          max = x-1
          t = nu
        print n, x-1
    return t

if __name__ == '__main__':
    a = time.time()
    print euler093()
    print "%f sec" % (time.time()-a)
