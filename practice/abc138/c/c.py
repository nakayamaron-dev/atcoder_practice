#!/usr/bin/env python3
N = int(input())
V = list(map(int, input().split()))

def solve():
    V.sort()
    for _ in range(N-1):
        avg = (V[0] + V[1]) / 2
        V.pop(0)
        V.pop(0)
        V.insert(0, avg)
    
    return V[0]

print(solve())

## AC
