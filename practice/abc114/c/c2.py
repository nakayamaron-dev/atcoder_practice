#!/usr/bin/env python3
# DFSで解く

# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

n = int(input())

# 数numについて調べ、末尾に数字を追加した数を再帰的に調べる関数
def dfs(num, use3, use5, use7):
    global ans
    if num > n: return
    
    # 3種類全て使っていたら答えに加算
    if use3 and use5 and use7:
        ans += 1
    
    dfs(10*num+3, True, use5, use7)
    dfs(10*num+5, use3, True, use7)
    dfs(10*num+7, use3, use5, True)

ans = 0
dfs(0, False, False, False)

print(ans)

# not self AC
# dfsを使わなければself AC
