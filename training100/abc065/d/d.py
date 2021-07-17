#!/usr/bin/env python3
from heapq import heappush, heappop, heapify
def main():
    N = int(input())
    X = []
    Y = []
    
    # x,y座標別々に取得してソートする。
    for i in range(N):
        x, y =  map(int,input().split())
        X.append((x, i))
        Y.append((y, i))
    
    X.sort()
    Y.sort()

    # 辺のコストを計算(ソート順で隣のものだけ取る)
    g = [[] for _ in range(N)]
    for i in range(N-1):
        cost = X[i+1][0] - X[i][0]
        g[X[i][1]].append((cost, X[i+1][1]))
        g[X[i+1][1]].append((cost, X[i][1]))

        cost = Y[i+1][0] - Y[i][0]
        g[Y[i][1]].append((cost, Y[i+1][1]))
        g[Y[i+1][1]].append((cost, Y[i][1]))
    
    # プリム法
    checked = [False] * N
    ans = 0
    q = []
    for i in g[0]:
        heappush(q, i)
    
    checked[0] = True
    cnt = 1

    while cnt < N:
        cost, node = heappop(q)
        if checked[node]:
            continue

        checked[node] = True
        cnt += 1
        ans += cost

        for c, n in g[node]:
            if checked[n]:
                continue

            heappush(q, (c, n))
    
    return ans

print(main())

