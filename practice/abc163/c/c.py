#!/usr/bin/env python3
import collections

n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = [0] * n

for idx, itm in c.items():
    ans[idx-1] = itm

for itm in ans:
    print(itm)

## AC