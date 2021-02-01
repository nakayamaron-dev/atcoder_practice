#!/usr/bin/env python3
n, m = map(int,input().split())
h = list(map(int, input().split()))
l = [list(map(int, input().split())) for l in range(m)]

observatories = [0] * n

# 良い展望台じゃない展望台を消していく。
for path in l:
    if h[path[0]-1] < h[path[1]-1]:
        observatories[path[0]-1] = 1
    elif h[path[0]-1] > h[path[1]-1]:
        observatories[path[1]-1] = 1
    else:
        observatories[path[0]-1] = 1
        observatories[path[1]-1] = 1

print(observatories.count(0))
    
## AC
