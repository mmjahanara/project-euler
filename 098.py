import time

def get_anagrams(file_name):
    with open(file_name) as f:
        line = f.readline()
    words = [w.strip('"') for w in line.strip().split(',')]
    ana = {}
    for w in words:
        key = ''.join(sorted(w))
        if not key in ana:
            ana[key] = []
        ana[key].append(w)
    return ana

def get_squares():
    sq = {x:set() for x in (2,3,4,5,6,7,8,9)}
    for x in range(4, 31623):
        s = x*x
        sq[len(str(s))].add(s)
    return sq

def get_init(word, num):
    res = {}
    str_num = str(num)
    for i, char in enumerate(word):
        if not char in res:
            res[char] = int(str_num[i])
        else:
            if not res[char] == str_num[i]: return {}
    return res

def get_number(word, mp):
    res = 0
    for x in word:
        res = res*10+mp[x]
    return res

def euler098():
    ana = get_anagrams('data/098words.txt')
    ana = {x:ana[x]  for x in ana if len(ana[x]) > 1} 

    square = get_squares()
    max_num = 0
    
    for key in ana:
        words = list(ana[key])
        numbers = square[len(key)]

        first_w = words[0]
        for this_num in numbers:
            mp = get_init(first_w, this_num)
            if mp == {}: continue
            if len(mp.keys()) != len(set(mp.values())): continue
            other_num = []
            for other in words[1:]:
                other_n = get_number(other, mp)
                other_num.append(other_n)
            sth_wrong = False
            for on in other_num:
                if not on in numbers:
                    sth_wrong = True
                    break
            if not sth_wrong: 
                print "%s %s %s" % (str(mp), str(words), str([this_num]+other_num))
                if max_num < max(other_num): max_num = max(other_num)
    return max_num

if __name__ == '__main__' :
    a = time.time()
    print euler098()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
