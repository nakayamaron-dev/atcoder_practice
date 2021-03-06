#!/usr/bin/env python3
from bisect import bisect_left,bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

# Bの要素を起点に、2分探索でAからB要素未満の値の数、Cから　B要素より大きい値の数をかけ合わせる。
for itm_b in B:
    idx_a = bisect_left(A, itm_b)
    idx_c = bisect_right(C, itm_b)

    ans += idx_a * (N - idx_c)

print(ans)

# not self AC    