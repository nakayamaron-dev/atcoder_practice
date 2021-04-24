#!/usr/bin/env python3
def calc_combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    W, H = map(int,input().split())
    mod = 10**9 + 7

    return calc_combinations_count(W+H-2, min(W, H)-1) % mod

print(main())

# self AC
