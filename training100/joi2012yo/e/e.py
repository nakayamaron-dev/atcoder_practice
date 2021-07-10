#!/usr/bin/env python3
from collections import deque
def main():
    W, H = map(int, input().split())

    # 外枠もカウントに含めるため、外側に空マスを用意する。
    L = [[0] + list(map(int, input().split())) + [0] for _ in range(H)]
    L = [[0]*(W+2)] + L + [[0]*(W+2)]

    # 遷移するパターンが奇数マス、偶数マスによって異なるため2パターン必要
    directions = [
        [(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(-1,0)],
        [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
        ]
    
    ans = 0
    q = deque()
    q.append((0, 0))
    L[0][0] = -1
    while q:
        x, y = q.popleft()
        for d in directions[y%2]:
            x2 = x + d[0]
            y2 = y + d[1]
            if 0 <= x2 <= W+1 and 0 <= y2 <= H+1:
                # ０のマスを進んでいき、周囲に1のマスがあればansをインクリメントする。
                if L[y2][x2] == 1:
                    ans += 1
                if L[y2][x2] == 0:
                    L[y2][x2] = -1
                    q.append((x2, y2))
    
    return ans

print(main())