#!/usr/bin/env python3
import statistics
N = int(input())
A = list(map(int, input().split()))

def f(n, arr):
    res = 0
    for idx, itm in enumerate(arr):
        res += abs(itm - (n+idx+1))    
    return int(res)

tmp = []
for idx, itm in enumerate(A):
    tmp.append(itm - (idx+1))

ans = f(statistics.median(tmp), A)
print(ans)

# not self AC
# 中央値が最適であることを直感で気付けるかどうか。
