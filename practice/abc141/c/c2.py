#!/usr/bin/env python3
from collections import Counter

N, K, Q = map(int,input().split())
A = [int(input()) for _ in range(Q)]

c = Counter(A)
for i in range(1, N+1):
    if K + c[i] - Q > 0:
        print("Yes")
    else:
        print("No")

## self AC
