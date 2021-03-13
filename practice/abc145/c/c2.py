#!/usr/bin/env python3
import math
def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

N = int(input())
XY = [list(map(int, input().split())) for l in range(N)]

permutations = permutations_array(range(N), N)
dists = []
for itm in permutations:
    dist = 0
    for i in range(len(itm)-1):
        From = XY[itm[i]]
        To = XY[itm[i+1]]
        dist += math.sqrt((From[0]-To[0])**2 + (From[1]-To[1])**2)
    
    dists.append(dist)

print(sum(dists)/len(dists))

## self AC
