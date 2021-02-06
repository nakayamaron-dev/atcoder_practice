#!/usr/bin/env python3
import numpy as np

n = int(input())
a = list(map(int, input().split()))

for idx, itm in enumerate(np.argsort(a)):
    if idx == n-1:
        print(itm+1)
    else:
        print(itm+1, end=' ')

 ## AC
