#!/usr/bin/env python3
from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

c = Counter(S)
values, counts = zip(*c.most_common())

maxnum = max(counts)
ans = []

for itm in c.items():
    if itm[1] == maxnum:
        ans.append(itm)

ans.sort(key=lambda x: x[0])

for itm in ans:
    print(itm[0])
        
## self AC
