#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())

    inf = float("inf")
    g = [[inf] * N for _ in range(N)]

    for _ in range(M):
        U, V, L = map(int,input().split())
        g[U-1][V-1] = L
        g[V-1][U-1] = L
    
    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    
    res = inf
    for i in range(1, N):
        for j in range(i+1, N):
              res = min(res, g[0][i] + g[i][j] + g[j][0])
    
    if res == inf:
        return -1
    else:
        return res

print(main())

# not self AC
# さっぱり分からない。
