import random

def pick_coin():
    s = ["HH", "HT", "TT"]
    return s[random.randint(0,2)]


def flip_coin(coin):
    sides = [coin[0], coin[1]]
    side = random.randint(0,1)
    return sides[side], sides[abs(1-side)]


def simulate():
    total = 0
    cnt = 0
    for i in range(10000000):
        coin = pick_coin()
        upside,downside = flip_coin(coin)
        if upside == "H":
            total += 1
            if downside == "T":
                cnt += 1
    print(cnt/total)
    print(total/10000000)
    print(cnt/10000000)

for i in range(100):
    print(random.randint(0,2))
simulate()


