#!/usr/bin/env python3
n, k, q = map(int,input().split())
a = [int(input()) for _ in range(q)]

scores = [0]*n

for itm in a:
    scores[itm-1] +=  1

for itm in scores:
    if k - q + itm <= 0:
        print('No')
    else:
        print('Yes')

## AC
