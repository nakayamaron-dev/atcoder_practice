#!/usr/bin/env python3
from collections import Counter
# 組み合わせ総数計算
def calc_combinations_count(n, r):
    import math
    if n < r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = int(input())
    A = list(map(int, input().split()))

    dic_0, dic_1 = {}, {}

    for key, val in Counter(A).items():
        dic_0[key] = calc_combinations_count(val, 2)
        dic_1[key] = calc_combinations_count(val-1, 2)
    
    Sum = sum(dic_0.values())
    for i in A:
        ans = 0
        ans += Sum - dic_0[i] + dic_1[i]
        print(ans)

main()
        
# self AC
