#!/usr/bin/env python3
def calc_lm(a,b):
    import math
    return int(a * b / math.gcd(a, b))

A, B = list(map(int, input().split()))

print(calc_lm(A,B))

## self AC
