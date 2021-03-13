#!/usr/bin/env python3
N, K = map(int,input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)

if K >= N:
    print(0)
else:
    print(sum(H[K:]))

## self AC
