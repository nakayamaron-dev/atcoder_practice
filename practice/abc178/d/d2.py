#!/usr/bin/env python3
def calc_combinations_count(n, r):
    import math
    if n < r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    S = int(input())
    max_cnt = S // 3
    ans = 0
    mod = 10**9 + 7

    if S < 3:
        return 0

    for i in range(1, max_cnt+1):        
        n = S - 3*i
        ans += calc_combinations_count(n+i-1, min(n, i-1))
        ans %= mod
    
    return ans

print(main())

# 惜しかった。
# 組み合わせの計算で工夫するところがわからなかった。
