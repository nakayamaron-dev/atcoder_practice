#!/usr/bin/env python3
def has_bit(n,i):
    return n&(1<<i)>0

N, M = map(int,input().split())
INF=float("INF")

#隣接グラフ作る
G = [[(INF,0) for _ in range(N)] for _ in range(N)]
for i in range(M):
    a, b, c, d=map(int,input().split())
    a -= 1
    b -= 1
    G[a][b] = (c, d)
    G[b][a] = (c, d)

Mx = 1 << N #集合の最大値
cost = [[INF] * N for _ in range(Mx)]
count = [[0] * N for _ in range(Mx)]

cost[0][0] = 0
count[0][0] = 1

for n in range(Mx):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            tmp = cost[n][i] + G[i][j][0]
            
            if tmp > G[i][j][1]:
                continue
            if tmp > cost[n|(1<<j)][j]:
                continue
            elif tmp < cost[n|(1<<j)][j]:
                count[n|(1<<j)][j] = 0
                cost[n|(1<<j)][j] = tmp
                
            count[n|(1<<j)][j] += count[n][i]

if count[Mx-1][0] == 0:
    print("IMPOSSIBLE")
else:
    print(cost[Mx-1][0], count[Mx-1][0])