#!/usr/bin/env python3
from collections import deque
def main():
    N = int(input())
    g = [[] for _ in range(N)]

    for _ in range(N-1):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    def bfs(x):
        q = deque()
        q.append(x)
        dist = [-1] * N
        dist[x] = 0

        while q:
            v = q.popleft()

            for nv in g[v]:
                if dist[nv] != -1:
                    continue

                dist[nv] = dist[v] + 1
                q.append(nv)
        
        return dist
    
    d = bfs(0)
    start = d.index(max(d))

    d = bfs(start)
    return max(d) + 1

print(main())