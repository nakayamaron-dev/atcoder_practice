#!/usr/bin/env python3
import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
minval = min(A, B, C, D, E)
ans = math.ceil(N/minval) + 4

print(ans)

# not self AC
# 発想力が大切
