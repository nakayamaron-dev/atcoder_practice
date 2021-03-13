#!/usr/bin/env python3
# 約数列挙
def get_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
divisors = get_divisors(N)

if len(divisors) % 2 == 0:
    a, b = divisors[len(divisors)//2 -1], divisors[len(divisors)//2]
    print(a+b-2)
else:
    a = divisors[len(divisors)//2]
    print(a*2-2)

## self AC
