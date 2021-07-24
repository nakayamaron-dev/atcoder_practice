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

            for i in g[v]:
                if dist[i] != -1:
                    continue

                dist[i] = dist[v] + 1
                q.append(i)
        
        return dist
    
    # start地点を決めるためのbfs
    d = bfs(0)
    start = d.index(max(d))

    # 決めたstartから始めた場合の最大距離を求める。
    d = bfs(start)

    # 一番遠いところから戻ってくるstartに戻ってくる道路を新設することが最適
    return max(d) + 1

print(main())

