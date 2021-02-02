#!/usr/bin/env python3
import math
from functools import reduce
k = int(input())
ans = 0

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

for a in range(1, k+1):
    for b in range(1, k+1):
        tmp = math.gcd(a,b)
        for c in range(1, k+1):
            ans += math.gcd(tmp, c)

print(ans)

## AC
