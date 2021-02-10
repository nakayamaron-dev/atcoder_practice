#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

mxg = mxp = cur = step = 0

for i in a:
    step += i
    mxp = max(mxp, step)
    mxg = max(mxg, cur+mxp)
    cur += step

print(mxg)

##
