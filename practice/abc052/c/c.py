#!/usr/bin/env python3
def calc_factorial(n):
    import math
    return math.factorial(n)

def main():
    N = int(input())
    mod = 10**9 + 7
    ans, cnt = 1, 1
    acm = calc_factorial(N)

    for i in range(2, N+1):
        # iがacmの素因数の場合
        while acm % i == 0:
            acm //= i
            cnt += 1
        
        ans *= cnt
        cnt = 1
    
    return ans % mod

print(main())

# not self AC
