#!/usr/bin/env python3
N = int(input())
D = list(map(int, input().split()))
D.sort()

l = D[len(D)//2 - 1]
r = D[len(D)//2]

print(r-l)

## self AC
