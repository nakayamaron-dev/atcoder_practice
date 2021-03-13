#!/usr/bin/env python3
def is_prime(n):
    import math
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0: return False
    return True

N = int(input())
while is_prime(N) == False:
    N += 1

print(N)

## self AC
