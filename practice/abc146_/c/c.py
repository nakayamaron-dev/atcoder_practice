#!/usr/bin/env python3
a, b, x = list(map(int, input().split()))

# 2分探索
minVal = 0
maxVal = 10**9 + 1

while maxVal - minVal > 1:
    half = (maxVal + minVal) // 2
    fee = a*half + b*len(str(half))
    if fee > x:
        maxVal = half
    else:
        minVal = half
    
print(minVal)