#!/usr/bin/env python3
from math import factorial
def main():
    N, M = map(int,input().split())
    mod = 10**9 + 7

    if abs(N-M) >= 2:
        return 0
    
    if abs(N-M) == 1:
        return factorial(N) * factorial(M) % mod
    
    if N == M:
        return factorial(N) * factorial(M) * 2  % mod
    
print(main())

# self AC
