#!/usr/bin/env python3
from collections import Counter
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
    N = int(input())
    f = prime_factorize(N)
    f = Counter(f)
    ans = 0
    
    for key, val in f.items():
        cnt = 1
        while val >= 0:
            val -= cnt
            cnt += 1
            ans += 1
        
        ans -= 1
    
    return ans

print(main())
    