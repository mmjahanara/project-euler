# ------------ NOT WORKING YET -------------------------


import time
import logging
from copy import deepcopy

logger = logging.getLogger('euler185')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fl = logging.FileHandler("log185.log")
fl.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
#logger.addHandler(ch)
logger.addHandler(fl)

class Node:
    def __init__(self, var_list):
        self.var_list = var_list

class Var:
    def __init__(self, domain):
        self.domain = domain

class Constraint:
    def __init__(self, test, num_correct):
        self.test, self.num_correct = test, num_correct

    def __repr__(self):
        return '%s: %s' % (str(self.test), str(self.num_correct))

def get_constraints(fn):
    res = []
    with open(fn, 'r') as f:
        for line in f:
            words = [w.strip() for w in line.split(';')]
            a = [int(x) for x in words[0]]
            b = words[1]
            constraint = Constraint(a, int(b))
            res.append(constraint)
    return res

seen = set()

def is_solution(node, constraints):
    for var in node.var_list:
        if len(var.domain) != 1:
            return False
    d = {i: list(node.var_list[i].domain)[0] for i in range(0, len(node.var_list))}
    key = ''.join(str(d[x]) for x in d)
    if key in seen:
        return False
    logger.debug(key)
    seen.add(key)
    for cons in constraints:
        x = reifi(d, cons.test)
        if x != cons.num_correct:
            return False
    return True


def reifi(d, test):
    s = 0
    for i in d:
        if d[i] == test[i]:
            s += 1
    return s


def propagate(node, constraints):
    d = dict()
    num_var = len(node.var_list)
    for i in range(0, num_var):
        var = node.var_list[i]
        if len(var.domain) == 1:
            d[i] = list(var.domain)[0]

    changed = True
    while changed:
        changed = False
        for con in constraints:
            num = reifi(d, con.test)
            if num > con.num_correct:
                return False
            elif num == con.num_correct:
                for i in range(0, num_var):
                    if i in d:
                        continue
                    dom = node.var_list[i].domain
                    if con.test[i] in dom:
                        dom.remove(con.test[i])
                        changed = True
                    if len(dom) == 0:
                        return False
            #continue
            #if 3 > 0:
                #pass
            elif num_var - len(d) == con.num_correct - num:
                for i in range(0, num_var):
                    var = node.var_list[i]
                    if len(var.domain) > 1:
                        var.domain = {con.test[i]}
                        d[i] = con.test[i]
                        changed = True
        #break
    return True


def get_children(node, constraints):
    res = []
    for i in range(0, len(node.var_list)):
        var = node.var_list[i]
        if len(var.domain) < 2:
            continue
        for value in var.domain:
            new_node = deepcopy(node)
            new_node.var_list[i].domain = {value}
            feasible = propagate(new_node, constraints)
            if feasible:
                res.append(new_node)
    return res

found = None


def solve(node, constraints):
    global found
    if found is not None:
        return
    if is_solution(node, constraints):
        found = node
        return
    children = get_children(node, constraints)
    for child in children:
        solve(child, constraints)
    return


def euler185():
    size, fn = 5, 'data/185_1.txt'
    #size, fn = 16, 'data/185.txt'
    constraints = get_constraints(fn)
    var_list = [Var(range(0, 10)) for _ in range(0, size)]
    node = Node(var_list)
    solve(node, constraints)
    d = found
    if d is None:
        return None
    else:
        key = ''.join(str(vl.domain) for vl in d.var_list)
        return key

if __name__ == '__main__':
    a = time.time()
    print euler185()
    print "time elapsed: %f millisec" % ((time.time()-a) * 1000)

