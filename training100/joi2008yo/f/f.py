#!/usr/bin/env python3
from heapq import heappop, heapify, heappush
def main():
    N, K = map(int,input().split())
    g = [[] for _ in range(N)]
    INF = float("inf")
    ans = []

    for _ in range(K):
        L = list(map(int, input().split()))
        t, a, b = L[:3]

        if t == 0:
            q = []
            q.append((0, a-1))
            dist = [INF] * N
            dist[a-1] = 0
            ok = [False] * N

            while not ok[b-1] and len(q) > 0:
                d, x = heappop(q)
                if d > dist[x] or ok[x]:
                    continue

                ok[x] = True

                for y, c in g[x]:
                    if ok[y]:
                        continue

                    if dist[y] > dist[x] + c:
                        dist[y] = dist[x] + c
                        heappush(q, (dist[y], y))
            
            if dist[b-1] == INF:
                ans.append(-1)
            else:
                ans.append(dist[b-1])
        
        else:
            c = L[3]
            g[a-1].append((b-1, c))
            g[b-1].append((a-1, c))
    
    # print(*ans, sep="\n")
    return ans

print(*main(), sep="\n")