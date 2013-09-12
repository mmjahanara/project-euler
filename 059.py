import time
import re

def euler059():
    with open('data/cipher1.txt') as f:
        ln = f.readline()
    cipher = map(int, ln.split(','))
    fac = len(cipher)/3 + 1

    with open('data/dict_en.txt') as f:
        ln = f.readlines()
    words = {x.strip().upper() for x in ln}

    rg = range(ord('a'), ord('z')+1)

    for a in rg:
        for b in rg:
            for c in rg:
                key = ([a,b,c]*fac)[:1201]
                decipher = ''.join([chr(x[0]^x[1]) for x in zip(key, cipher)])
                up_set = set(re.sub(r'\W', ' ', decipher.upper()).split())
                if len(up_set.intersection(words)) < .5 * len(up_set): continue
                print decipher 
                print sum(map(ord, decipher))

if __name__ == '__main__':
    a = time.time()
    euler059()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
