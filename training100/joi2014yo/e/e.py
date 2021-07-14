#!/usr/bin/env python3
from heapq import heappop, heappush
def main():
    N, K = map(int,input().split())
    C = [tuple(map(int,input().split())) for i in range(N)]
    g = [[] for _ in range(N)]
    INF = float("inf")

    for _ in range(K):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    h = [[0, 0, 0]]

    while h:
        d, k, now = heappop(h)

        if dist[now][k] != d:
            continue

        c, nk = C[now]

        for nex in g[now]:
            if dist[nex][nk-1] > d+c:
                dist[nex][nk-1] = d+c
                heappush(h, [d+c, nk-1, nex]) 
        
        if k == 0:
            continue

        for nex in g[now]:
            if dist[nex][k-1] > d:
                dist[nex][k-1] = d
                heappush(h, [d, k-1, nex])
    
    return min(dist[-1])

print(main())
    
    