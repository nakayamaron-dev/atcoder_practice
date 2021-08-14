#!/usr/bin/env python3
def gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    return gcd(*A)

print(main())