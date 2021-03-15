#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

Max = 10**6 + 1
cnt = [0]*Max
for i in A:
    if cnt[i] != 0:
        cnt[i] = 2
        continue

    for j in range(i, Max, i):
        cnt[j] += 1
    
ans = 0
for a in A:
    if cnt[a] == 1:
        ans += 1

print(ans)

# not self AC
# Aの要素をイテレートして、その倍数の場所をインクリメントしていく。
# 計算量を正しく見積もることができるかが重要
# 入力に重複ありのパターンに注意
