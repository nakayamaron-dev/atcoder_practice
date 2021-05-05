#!/usr/bin/env python3
from collections import deque
def main():
    N, X, Y = map(int,input().split())
    g = [[] for _ in range(N)]

    for i in range(N-1):
        g[i].append(i+1)
        g[i+1].append(i)
    
    g[X-1].append(Y-1)
    g[Y-1].append(X-1)

    ans = [0] * N

    # bfs
    for i in range(N-1):
        q = deque()
        q.append(i)
        dist = [-1] * N
        dist[i] = 0

        while q:
            now = q.popleft()
            for nxt in g[now]:
                # まだ訪れていない場合
                if dist[nxt] == -1:
                    dist[nxt] = dist[now] + 1
                    q.append(nxt)
        
        for j in range(i+1, N):
            ans[dist[j]] += 1
    
    for i in range(1, N):
        print(ans[i])
    
main()

# not self AC
# 幅優先探索
