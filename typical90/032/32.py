#!/usr/bin/env python3
from itertools import permutations
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    g = [[False]*(N+1) for _ in range(N+1)]
    INF = float("inf")
    ans = INF

    for _ in range(M):
        x, y = map(int,input().split())
        x, y = x-1, y-1
        g[x][y] = True
        g[y][x] = True

    for order in permutations(range(N)):

        for x, y in zip(order, order[1:]):
            if g[x][y] or g[y][x]:
                break
        else:
            tmp = 0
            for idx, itm in enumerate(order):
                tmp += A[itm][idx]
            
            ans = min(ans, tmp)
    
    return -1 if ans == INF else ans

print(main())