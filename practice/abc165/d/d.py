#!/usr/bin/env python3
A, B, N = map(int,input().split())

if N >= B:
    x = B - 1
else:
    x = N

ans = (A*x // B)
print(ans)

# self AC
