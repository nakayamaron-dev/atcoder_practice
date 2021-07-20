#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)

def main():
    N = int(input())
    g = [[] for _ in range(N)]

    for _ in range(N-1):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    color = [-1] * N

    # 再帰dfs
    def dfs(node, c):
        color[node] = c
        for nxt in g[node]:
            if color[nxt] != -1:
                continue
            dfs(nxt, not c)
    
    dfs(0, True)
    cnt = sum(color)

    if cnt >= N//2:
        return [i+1 for i in range(N) if color[i]][:N//2]
    else:
        return [i+1 for i in range(N) if not color[i]][:N//2]

print(*main())

# 二部グラフ
# 塗り分けたときに、どちらかは//2以上