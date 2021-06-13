#!/usr/bin/env python3
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

K = int(input())
MAX = 3234566667
ans = []

def dfs(n):
    global ans

    # nが問題の上限を超えていたら終了。
    if n > MAX: return

    ans.append(n)

    # 一の位
    ichi = n % 10

    # 同じ数字の場合
    dfs(n*10 + ichi)

    # 1以上であれば、1小さい数が可能
    if ichi > 0:
        dfs(n*10 + ichi - 1)
    
    # 8以下であれば、1大きい数が可能
    if ichi < 9:
        dfs(n*10 + ichi + 1)

#先頭の数字が1~9の場合それぞれについてdfsを実行する。
for i in range(1, 10):
    dfs(i)

ans.sort()
print(ans[K-1])

