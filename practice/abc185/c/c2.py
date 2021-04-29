#!/usr/bin/env python3

# 組み合わせ総数計算
def calc_combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def solve():
    N = int(input())
    return calc_combinations_count(N-1, 11)

print(solve())

# self AC
# 組み合わせ総数を計算できればとても簡単。