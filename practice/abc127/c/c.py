#!/usr/bin/env python3
N, M = map(int,input().split())

minval = 0
maxval = 10**5 + 1
for _ in range(M):
    L, R = map(int,input().split())
    minval = max(minval, L)
    maxval = min(maxval, R)

if minval > maxval:
    print(0)
else:
    print(maxval - minval + 1)

# self AC
