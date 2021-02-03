#!/usr/bin/env python3
n, k = map(int,input().split())
h = list(map(int, input().split()))

h = sorted(h, reverse=True)
del h[0:k]
print(sum(h))

## AC
