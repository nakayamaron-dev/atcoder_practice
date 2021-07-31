#!/usr/bin/env python3
def gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    A, B, C = map(int,input().split())

    GCD = gcd(A, B, C)

    return (A+B+C) // GCD -3

print(main())