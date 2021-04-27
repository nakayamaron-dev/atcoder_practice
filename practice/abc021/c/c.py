#!/usr/bin/env python3
from collections import deque
def main():
    N = int(input())
    A, B = map(int,input().split())
    M = int(input())
    mod = 10**9 + 7
    
    g = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    
    dist = [-1] * (N+1)
    dist[0] = 0
    dist[A] = 0

    #各頂点までのaからの最短経路数を記録。distが 3, 4 なら、大きい4のほうの点に経路数を足していく。
    p = [0]*(N+1)
    p[A] = 1

    d= deque()
    d.append(A)

    while d:
        v = d.popleft()
        for i in g[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                d.append(i)
            
            if dist[i] == dist[v] + 1:
                p[i] += p[v]
    
    return p[B] % mod

print(main())

# not self AC
# さっぱり分からない。
