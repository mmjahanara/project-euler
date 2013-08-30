from collections import Counter
def e059():
    with open('data/cipher1.txt') as f:
        ln = f.readline()
    cipher = map(int, ln.split(','))
    fac = len(cipher)/3 + 1

    #etao = 'ETAOINSHRDLU'
    rg = range(ord('a'), ord('z')+1)
    fout = open('out.txt', 'w')

    for a in rg:
        for b in rg:
            for c in rg:
                key = ([a,b,c]*fac)[:1201]
                decipher = [chr(x[0]^x[1]) for x in zip(key, cipher)]
                dcstr = ''.join(decipher)
                upp = dcstr.upper()
                cntr = Counter(upp)
                if (upp.find('THE') < 0): continue
                if (upp.find('OF') < 0): continue
                if (upp.find('IN') < 0): continue
                fout.write(dcstr+'\n')
    fout.close()

if __name__ == '__main__':
    e059()
