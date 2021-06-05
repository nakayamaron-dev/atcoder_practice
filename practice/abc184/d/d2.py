#!/usr/bin/env python3
from functools import lru_cache
def main():
    A, B, C = map(int,input().split())

    @lru_cache(maxsize=None)
    def rec(a, b, c):
        if a == 100 or b == 100 or c == 100:
            return 0
        
        s = a + b + c
        select_a = a/s * (rec(a+1, b, c) + 1) 
        select_b = b/s * (rec(a, b+1, c) + 1) 
        select_c = c/s * (rec(a, b, c+1) + 1) 

        return select_a + select_b + select_c
    
    return rec(A, B, C)

print(main())

# 確率DP
# rec(a, b, c) : コインがa, b, c枚の場合の答え
# メモ化再帰を使って実装

