#!/usr/bin/env python3
import math
l = int(input())
n = 1

for i in range(l - 11, l):
    n *= i

ans = n // math.factorial(11)
print(ans)

## AC
