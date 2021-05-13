#!/usr/bin/env python3
def gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list

def main():
    A, B = map(int,input().split())
    x = gcd(A, B)

    divs = set(prime_factorize(x))
    return len(divs) + 1

print(main())

# not self AC
# 最大公約数の素因数の個数+1が答えになる。
