#!/usr/bin/env python3
K, N = map(int,input().split())
A = list(map(int, input().split()))

dims = []
for idx in range(len(A)):
    if idx == len(A)-1:
        dim = K - (A[-1] - A[0])
        dims.append(dim)
    else:
        dim = A[idx+1] - A[idx]
        dims.append(dim)

ans = K - max(dims)
print(ans)

## self AC
