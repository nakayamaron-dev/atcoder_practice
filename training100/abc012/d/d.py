#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    INF = float("inf")
    g = [[INF] * N for _ in range(N)]
    ans = INF

    for _ in range(M):
        A, B, T = map(int,input().split())
        A, B = A-1, B-1

        g[A][B] = T
        g[B][A] = T
    
    for i in range(N):
        g[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                # kが中継点であり、中継点を全通り試す。
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    
    for i in range(N):
        ans = min(ans, max(g[i]))
    
    return ans

print(main())
