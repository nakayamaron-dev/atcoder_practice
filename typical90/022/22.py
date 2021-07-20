#!/usr/bin/env python3
def gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    A, B, C = map(int,input().split())

    g = gcd(A, B, C)
    
    # それぞれの辺で何個作れるか
    return (A // g - 1) + (B // g - 1) + (C // g - 1)

print(main())