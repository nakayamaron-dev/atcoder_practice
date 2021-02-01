#!/usr/bin/env python3
import itertools
n, m, x = map(int,input().split())
l = [list(map(int, input().split())) for l in range(n)]

ptn = list(itertools.product("YN", repeat=n))
moneys = []

#全探索で解く
for itm in ptn:
    money = 0
    skills = [0] * n
    for idx, i in enumerate(itm):
        if i == 'Y':
            money += l[idx][0]
            skills = [x + y for (x, y) in zip(skills, l[idx][1:])]

    if min(skills) >= x:
        moneys.append(money)

if len(moneys) == 0:
    print(-1)
else:
    print(min(moneys))

## AC
