#!/usr/bin/env python3
# 方針
# 累積の最高値を記録し、次の身長が最高値以下であれば、最高値と同じになるまでの台座を用意する。

N = int(input())
A = list(map(int, input().split()))

maxval = 0
ans = 0

for i in range(1, N):
    maxval = max(maxval, A[i-1])

    if A[i] < maxval:
        ans += maxval - A[i]

print(ans)

## self AC
