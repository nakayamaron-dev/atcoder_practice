#!/usr/bin/env python3
import collections
N = int(input())
A = list(map(int, input().split()))

ans = [0]*N
counter = collections.Counter(A)

for idx, itm in counter.items():
    ans[idx-1] = itm

for itm in ans:
    print(itm)

## self AC
