#!/usr/bin/env python3
import itertools
import math

n = int(input())
xy = [list(map(int, input().split())) for l in range(n)]

order = list(itertools.permutations(range(n), n))
dist = 0

for ptn in order:
    for i in range(n-1):
        dist += math.sqrt((xy[ptn[i+1]][0] - xy[ptn[i]][0])**2 + (xy[ptn[i+1]][1] - xy[ptn[i]][1])**2)

print(dist / len(order))
        
## AC
