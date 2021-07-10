#!/usr/bin/env python3
from collections import deque
def main():
    R, C = map(int,input().split())
    SY, SX = map(int,input().split())
    GY, GX = map(int,input().split())
    S = [input() for _ in range(R)]

    # start, goalの座標調整
    SY -= 1
    SX -= 1
    GY -= 1
    GX -= 1

    # 訪問したかどうかを管理する配列
    dist = [[-1]*C for _ in range(R)]

    q = deque()
    q.append([SX, SY])
    dist[SY][SX] = 0

    while len(q) > 0:
        px, py = q.popleft()

        # 隣接する4マスをイテレート
        for x, y in [[px+1, py],[px-1, py],[px, py+1],[px, py-1]]:

            if not (0 <= x < C and 0 <= y < R):
                continue

            if S[y][x] == "#":
                continue

            if dist[y][x] == -1:
                dist[y][x] = dist[py][px] + 1
                q.append([x, y])
    
    return dist[GY][GX]

print(main())
