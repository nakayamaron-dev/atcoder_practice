#!/usr/bin/env python3
def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    return get_gcd(*a)

print(main())

# not self AC
# 答えが最大公約数になると理解するのが難しい。
