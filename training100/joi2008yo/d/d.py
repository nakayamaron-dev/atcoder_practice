#!/usr/bin/env python3
def main():
    M = int(input())
    LM = [list(map(int, input().split())) for _ in range(M)]
    N = int(input())
    LN = [list(map(int, input().split())) for _ in range(N)]
    LM.sort()
    point = LM[0]

    for i in range(N):
        mx = LN[i][0] - point[0]
        my = LN[i][1] - point[1]

        for x, y in LM:
            if [x + mx, y + my] not in LN:
                break
        else:
            return mx, my 

print(*main())