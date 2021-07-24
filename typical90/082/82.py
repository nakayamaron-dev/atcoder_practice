#!/usr/bin/env python3
def sum_tosa(n):
    return n * (n+1) // 2

def main():
    L, R = map(int,input().split())
    MOD = 10**9 + 7
    l = len(str(L))
    r = len(str(R))
    ans = 0

    for i in range(l, r+1):
        ans += i * (sum_tosa(min(10**i - 1, R)) - sum_tosa(max(10**(i-1), L) - 1))
        ans %= MOD
    
    return ans

print(main())