import math


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

    rotation = [90, 180, 270, 360]
    tp.sort()
    sp.sort()

    if len(tp) != len(sp):
        return "No"

    for rot in rotation:
        spr = []
        for s in sp:
            cos = math.cos(math.radians(rot))
            sin = math.sin(math.radians(rot))
            sx = round(s[0] * cos - s[1] * sin, 2)
            sy = round(s[0] * sin + s[1] * cos, 2)
            spr.append((sx, sy))

        ans = set()
        spr.sort()
        for i in range(len(spr)):
            ans.add((tp[i][0] - spr[i][0], tp[i][1] - spr[i][1]))

        if len(ans) == 1:
            return "Yes"

    return "No"


print(main())
