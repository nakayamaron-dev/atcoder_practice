#!/usr/bin/env python3
k, n = map(int,input().split())
a = list(map(int, input().split()))
dist = []

for i in range(n):
    if i == n - 1:
        dist.append(a[0]+(k - a[i]))
    else:
        dist.append(a[i+1] - a[i])

print(k - max(dist))

## AC
