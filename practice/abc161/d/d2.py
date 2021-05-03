#!/usr/bin/env python3
# DFSで解く

# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

k = int(input())
MAX = 3234566667
ans = []

def dfs(n):
    global ans

    if n > MAX: return

    ans.append(n)

    # 一の位の数字
    ichi = n % 10

    # 同じ数字の場合
    dfs(n*10 + ichi)
    
    # 1以上8以下の場合、-1と+1の2通りdfsを実行する。
    if ichi > 0:
        dfs(n*10 + ichi - 1)
    if ichi < 9:
        dfs(n*10 + ichi + 1)

for i in range(1, 10):
    dfs(i)

ans.sort()
print(ans[k-1])

# not self AC
# MAXの値は問題の例からとってくる。
