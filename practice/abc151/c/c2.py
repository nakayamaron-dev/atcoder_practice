#!/usr/bin/env python3
N, M = map(int,input().split())

wa = [0]*N
ac = [0]*N
pena = 0

for _ in range(M):
    prob, res = input().split()
    prob = int(prob) - 1

    if ac[prob] == 0 and res == "AC":
        ac[prob] = 1
        pena += wa[prob]
    elif ac[prob] == 0 and res == "WA":
        wa[prob] += 1
    
print(sum(ac), pena)

## self AC
