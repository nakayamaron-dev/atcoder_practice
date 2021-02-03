#!/usr/bin/env python3
n = int(input())
x = list(map(int, input().split()))

min_dist = 0

for p in range(1, 101):
    dist = 0
    for xpoint in x:
        dist += (xpoint - p)**2

    if p == 1:
        min_dist = dist
    else:
        if dist < min_dist:
            min_dist = dist

print(min_dist)

## AC
