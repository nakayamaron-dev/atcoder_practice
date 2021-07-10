#!/usr/bin/env python3
from collections import deque
def main():
    H, W, N = map(int,input().split())
    S = [input() for _ in range(H)]
    ans = 0

    for i in range(H):
        if "S" in S[i]:
            sy = i
            sx = S[i].index("S")
            S[i] = S[i].replace("S", "0")
        
    for start in range(N):
        q = deque()
        q.append([sx, sy])
        dist = [[-1]*W for _ in range(H)]
        dist[sy][sx] = 0
        ps = start + 1
        flag = False

        while len(q) > 0:
            px, py = q.popleft()

            for x, y in [[px+1, py], [px-1, py], [px, py+1], [px, py-1]]:
                if not (0 <= x < W and 0 <= y < H):
                    continue

                if S[y][x] == "X":
                    continue

                if dist[y][x] == -1:
                    dist[y][x] = dist[py][px] + 1
                    q.append([x, y])
                
                if S[y][x].isdigit() and int(S[y][x]) == ps:
                    sx, sy = x, y
                    ans += dist[y][x]
                    flag = True
                    break

            if flag:
                break
    
    return ans

print(main())

# 巣、S
# チーズ工場、数字
# 障害物、X
# 空き地、.
# チーズを小さい順番に食べていく。

