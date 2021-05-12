#!/usr/bin/env python3
from bisect import bisect_left
def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0

    for a in range(N-2):
        for b in range(a+1, N-1):
            # cはL[a]+L[b]を超えない最大値までのindex
            c = bisect_left(L, L[a]+L[b])
            ans += c - b - 1
    
    return ans

print(main())

# not self AC
# 全探索し、O(N^3)だと間に合わないので、Lをソートしておいて3本目の選び方を２分探索で探すことで計算量を調整する。
