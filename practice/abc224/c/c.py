#!/usr/bin/env python3

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(2, N):
        x1, y1 = XY[i]
        for j in range(i):
            x2, y2 = XY[j]
            for k in range(j):
                x3, y3 = XY[k]
                if (y2-y1)*(x3-x1) != (x2-x1)*(y3-y1):
                    ans += 1

    return ans


print(main())
