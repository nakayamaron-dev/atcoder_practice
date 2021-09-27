#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    SUM = sum(A)
    cnt = (X // SUM) * N
    X -= (X // SUM) * SUM

    for a in A:
        X -= a
        cnt += 1

        if X < 0:
            return cnt


print(main())
