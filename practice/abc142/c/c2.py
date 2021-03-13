#!/usr/bin/env python3
import numpy as np

N = int(input())
A = list(map(int, input().split()))

ans = np.argsort(A)
print(" ".join([str(i+1) for i in ans]))

## self AC
