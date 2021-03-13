#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))

ans = 0
minval = 10**9

for p in P:
    minval = min(minval, p)
    if minval == p:
        ans += 1

print(ans)

## self AC
