import re

def e059():
    with open('data/cipher1.txt') as f:
        ln = f.readline()
    cipher = map(int, ln.split(','))
    fac = len(cipher)/3 + 1

    with open('data/dict_en.txt') as f:
        ln = f.readlines()
    words = {x[:-1].upper() for x in ln}

    rg = range(ord('a'), ord('z')+1)

    for a in rg:
        for b in rg:
            for c in rg:
                key = ([a,b,c]*fac)[:1201]
                decipher = ''.join([chr(x[0]^x[1]) for x in zip(key, cipher)])
                up_list = re.sub(r'\W', ' ', decipher.upper()).split()
                x = [1 if w in words else 0 for w in up_list]
                if sum(x) < .8 * len(up_list): continue
                print decipher 
                print sum(map(ord, decipher))

if __name__ == '__main__':
    e059()
