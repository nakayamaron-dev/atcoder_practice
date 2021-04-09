#!/usr/bin/env python3
def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

N, X = map(int,input().split())
L = list(map(int, input().split()))

for i in range(N):
    L[i] = abs(L[i] - X)

ans = get_gcd(*L)
print(ans)

# self AC
