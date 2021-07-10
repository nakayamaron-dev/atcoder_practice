#!/usr/bin/env python3
from collections import deque
def main():
    W, H = map(int,input().split())
    L = [list(map(int, input().split())) for _ in range(H)]
    ans = 0

    q = deque()
    q.append([0,0])
    visited = [[False]*W for _ in range(H)]

    while len(q) > 0:
        cx, cy = q.popleft()

        for x, y in [[cx+1, cy],[cx-1, cy-1],[cx-1, cy],[cx-1, cy-1],[cx, cy-1],[cx, cy+1]]:
            if not (0 < x <= W and 0 < y <= H):
                continue

            if visited[y][x] == False:
                q.append([x, y])
                visited[y][x] = True

                if L[y][x] != L[cy][cy]:
                    ans += 1
    
    return ans

print(main())