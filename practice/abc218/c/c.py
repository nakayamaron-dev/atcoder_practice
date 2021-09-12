#!/usr/bin/env python3
def rotation(point, degree):
    import math
    cos = math.cos(math.radians(degree))
    sin = math.sin(math.radians(degree))
    x = round(point[0] * cos - point[1] * sin, 2)
    y = round(point[0] * sin + point[1] * cos, 2)

    return (x, y)


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    sp = []
    tp = []

    for i in range(N):
        for j in range(N):
            if S[N - (i+1)][j] == "#":
                sp.append((j, i))

            if T[N - (i+1)][j] == "#":
                tp.append((j, i))

    tp.sort()
    sp.sort()

    if len(tp) != len(sp):
        return "No"

    for rot in [90, 180, 270, 360]:
        spr = []
        for s in sp:
            spr.append(rotation(s, rot))

        ans = set()
        spr.sort()
        for i in range(len(spr)):
            ans.add((tp[i][0] - spr[i][0], tp[i][1] - spr[i][1]))

        if len(ans) == 1:
            return "Yes"

    return "No"


print(main())
