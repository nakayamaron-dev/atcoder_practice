#!/usr/bin/env python3
N = int(input())
A = [int(input()) for _ in range(N)]

maxval = max(A)
AA = sorted(A, reverse=True)

for i in range(N):
    if A[i] == maxval:
        print(AA[1])
    else:
        print(maxval)

## self AC
