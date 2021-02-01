#!/usr/bin/env python3
import itertools
n, m, q = map(int,input().split())
abcd = [list(map(int, input().split())) for l in range(q)]

seq = tuple(range(1,m+1))
ptn = list(itertools.combinations_with_replacement(seq, n))
max_score = 0

# 全探索で解く
for itm in ptn:
    score = 0
    for i in abcd:
        if itm[i[1] - 1] - itm[i[0] - 1] == i[2]:
            score += i[3]
    
    if score > max_score:
        max_score = score

print(max_score)
        
## AC
