#!/usr/bin/env python3
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

def main():
    N = int(input())
    
    child = [[] for _ in range(N)]
    for i in range(1, N):
        b = int(input())
        child[b-1].append(i)
    
    # dfs[i]: 頂点iの子の給料を全て求め、自身の給料を計算して返す。
    def dfs(i):
        #子がいなければ１
        if len(child[i]) == 0:
            return 1
        else:
            v = []
            for j in child[i]:
                v.append(dfs(j))
            
            return max(v) + min(v) + 1
    
    return dfs(0)

print(main())

# not self AC
# 木に対する動的計画法。再帰関数で必要な値を返しながら深さ優先探索(dfs)していく
