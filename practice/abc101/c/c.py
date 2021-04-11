#!/usr/bin/env python3
import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(math.ceil((N-1)/(K-1)))

# not self AC
# 一度に変更できるのはK-1個の数字、変えるべき数字はN-1個、N-1個の数字をK-1個ずつ変える場合の回数を求めればよい。