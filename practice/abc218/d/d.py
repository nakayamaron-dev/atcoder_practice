#!/usr/bin/env python3
def main():
    N = int(input())
    P = set(tuple(map(int, input().split())) for _ in range(N))
    ans = 0

    for x1, y1 in P:
        for x2, y2 in P:
            if not(x1 < x2 and y1 < y2):
                continue

            q = (x1, y2)
            r = (x2, y1)

            if q in P and r in P:
                ans += 1

    return ans


print(main())
