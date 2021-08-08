#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    G=[[] for _ in range(N+1)]

    for _ in range(N-1):
        A, B = map(int,input().split())
        G[A].append(B)
        G[B].append(A)
    
    for i in range(N+1):
        G[i].sort()
    
    ans = []
    def dfs(pre, cur):
        # 開始時にリストに追加
        ans.append(cur)
        for nxt in G[cur]:
            if nxt != pre:
                dfs(cur, nxt)

                # 終了時にもリストに追加(ここがポイント)
                ans.append(cur)
    
    dfs(-1, 1)
    return ans

print(*main())