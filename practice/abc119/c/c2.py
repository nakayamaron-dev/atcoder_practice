#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def main():
    N, A, B, C = map(int,input().split())
    L = [int(input()) for _ in range(N)]
    INF = float("inf")

    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                # 最初の1本目の合成MPは必要ないため、最後に30を引く。
                return abs(a - A) + abs(b - B) + abs(c - C) - 30 
            else:
                return INF
        
        # curの竹を使わない場合
        ret0 = dfs(cur + 1, a, b, c)

        # 10MP消費し、竹を接合する場合
        ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10
        
        return min(ret0, ret1, ret2, ret3)
    
    return dfs(0, 0, 0, 0)

print(main())