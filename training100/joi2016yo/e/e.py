#!/usr/bin/env python3
from collections import defaultdict, deque

def main():
    N, M, K, S = map(int,input().split())
    P, Q = map(int,input().split())
    C = set([int(input()) - 1 for _ in range(K)])
    G = defaultdict(list)
    INF = float("inf")

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)
    
    # 距離管理？
    dists = [INF] * N
    q = deque([(c, 0, 0) for c in C])

    # 危険地を起点として幅優先探索
    while q:
        v, dist, dep = q.pop()
        if dep > S or dists[v] <= dist:
            continue

        dists[v] = dist
        for _v in G[v]:
            q.append((_v, dist+1, dep+1))
    
    # 宿泊費を管理する配列（最初は全てP円にしておく）
    V = [P] * N

    # 危険地から近いエリアの宿泊費をQ円に更新
    for i, dist in enumerate(dists):
        if dist <= S:
            V[i] = Q
    
    # スタートとゴール地点は宿泊しない。
    V[0] = V[-1] = 0

    dists = [INF] * N
    q = deque([(0, 0)])

    # スタートを起点として幅優先探索
    while q:
        v, c = q.popleft()
        if dists[v] <= c:
            continue

        dists[v] = c

        for _v in G[v]:
            if _v not in C:
                q.append((_v, c+V[_v]))
    
    return dists[-1]

print(main())
