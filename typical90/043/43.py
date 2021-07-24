#!/usr/bin/env python3
from collections import deque
def main():
    H, W = map(int,input().split())
    RS, CS = map(int,input().split())
    RT, CT = map(int,input().split())
    S = [input() for _ in range(H)]
    RS, CS = RS-1, CS-1
    RT, CT = RT-1, CT-1

    # 下、左、上、右
    dh = [-1, 0, 1, 0]
    dw = [0, -1, 0, 1]

    dist = [[[float("inf")]*4 for _ in range(W)] for _ in range(H)]
    q = deque()

    for i in range(4):
        dist[RS][CS][i] = 0
        q.append([RS, CS, i])

    while q:
        h, w, i = q.popleft()
        stay = dist[h][w][i]
        step = stay + 1

        if (h, w) == (RT, CT):
            return stay
        
        for j in range(4):
            dist[h][w][j] = min(dist[h][w][j], step)
        
        for j in range(4):
            nh, nw = h + dh[j], w + dw[j]
            if not (0 <= nh < H and 0 <= nw < W):
                continue

            if S[nh][nw] == "#":
                continue

            cost = stay if i == j else step

            if dist[nh][nw][j] <= cost:
                continue

            dist[nh][nw][j] = cost

            q.appendleft([nh, nw, j]) if i == j else q.append([nh, nw, j])

print(main())
