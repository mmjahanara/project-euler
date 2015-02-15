import time

def change(money, coins):
    if len(coins)==0: return 0
    elif len(coins) == 1: return 1 if money / coins[0] * coins[0] == money else 0
    else: return sum(change(money-i*coins[0], coins[1:]) for i in range(0, money/coins[0]+1))

def euler031():
    return change(500, [200,100,50,20,10,5,2,1])

if __name__ == "__main__":
    a = time.time()
    print euler031()
    print "time elapsed: %f millisec" % ((time.time()-a)*1000)
