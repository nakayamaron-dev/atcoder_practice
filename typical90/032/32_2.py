#!/usr/bin/env python3
def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    g = [[False]*(N+1) for _ in range(N+1)]
    INF = float('inf')
    ans = INF

    for _ in range(M):
        X, Y = map(int,input().split())
        X, Y = X-1, Y-1
        g[X][Y] = True
        g[Y][X] = True
    
    for ptn in permutations_array(range(N), N):
        for cur, nxt in zip(ptn, ptn[1:]):
            if g[cur][nxt] or g[nxt][cur]:
                break
        else:
            tmp = 0
            for idx, itm in enumerate(ptn):
                tmp += A[itm][idx]
            
            ans = min(tmp, ans)
    
    return -1 if ans == INF else ans

print(main())