#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

#Aの最大公約数が答え
print(get_gcd(*A))

#not self AC
