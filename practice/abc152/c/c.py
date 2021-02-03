#!/usr/bin/env python3
n = int(input())
p = list(map(int, input().split()))
ans = 1
minVal = 0

for i in range(n):
    if i == 0:
        minVal = p[i]
    else:
        if p[i] <= minVal:
            minVal = p[i]
            ans += 1

print(ans)

## AC
