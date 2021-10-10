#!/usr/bin/env python3
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
ans = 0


def dfs(c, i):
    global ans

    print("i: ", i)
    print("C: ", c)
    print("Min: ", max(A[i], c), "Max: ", B[i])

    if i == N-1:
        ans += B[i] - max(A[i], c) + 1
        print("ans: ", ans)
        return

    for j in range(max(A[i], c), B[i]+1):
        print("J: ", j)
        dfs(j, i+1)


# 先頭の数字毎にDFS (ルンルン数 abc161)
for i in range(A[0], B[0]+1):
    dfs(i, 0)

print(ans % MOD)
