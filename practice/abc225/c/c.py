#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]

    for i in range(M):
        if B[0][i] % 7 == 0 and i != M-1:
            return "No"

    for i in range(N):
        for j in range(M-1):
            if B[i][j+1] - B[i][j] != 1:
                return "No"

    for i in range(N-1):
        for j in range(M):
            if B[i+1][j] - B[i][j] != 7:
                return "No"

    return "Yes"


print(main())
