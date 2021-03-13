#!/usr/bin/env python3
N = int(input())
V = list(map(int, input().split()))
V.sort()

for i in range(len(V)-1):
    avg = (V[0] + V[1]) / 2
    V.pop(0)
    V.pop(0)
    V.insert(0, avg)

print(V[0])

## self AC
