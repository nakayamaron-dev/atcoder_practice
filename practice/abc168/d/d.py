#!/usr/bin/env python3
from collections import deque

N, M = map(int,input().split())
edge = [set() for _ in range(N)]

for _ in range(M):
     A, B = map(int, input().split())
     A -= 1
     B -= 1
     edge[A].add(B)
     edge[B].add(A)

# depth:部屋１から各部屋への深さ（部屋１の深さは０）
depth = [float('inf')] * N
prev = [0] * N

# キューの要素：(部屋,深さ)
q = deque()
depth[0] = 0
q.append((0, 0))

# BFS
while q:
    v, s = q.popleft()
    ns = s + 1
    for nv in edge[v]:
        if depth[nv] > ns:
            depth[nv] = ns
            prev[nv] = v
            q.append((nv, ns))

print('Yes')
for i in range(N-1):
    print(prev[i + 1] + 1)

# 幅優先探索 (breadth-first search, BFS)
