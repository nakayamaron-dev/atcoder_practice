#!/usr/bin/env python3
def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    A, B = map(int,input().split())
    x = get_gcd(A, B)
    ans = 1

    for i in range(2, x):
        if i * i > x: break
        if x % i: continue

        ans += 1
        while x % i == 0:
            x //= i
    
    if x > 1:
        ans += 1
    
    return ans

print(main())

# not self AC
# 途中
