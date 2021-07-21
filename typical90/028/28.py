#!/usr/bin/env python3

# 座標の最大値(max)、本当は1000だけど余裕をとって+5
mx = 1002
t = [[0]*mx for _ in range(mx)]

n = int(input())
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    # 左下と右上は+1、左上と右下は-1
    t[lx][ly] += 1
    t[rx][ry] += 1
    t[lx][ry] -= 1
    t[rx][ly] -= 1

# y軸方向に累積和
for x in range(mx):
    for y in range(mx-1):
        t[x][y+1] += t[x][y]

# x軸方向に累積和
for y in range(mx):
    for x in range(mx-1):
        t[x+1][y] += t[x][y]

# 重なっている枚数別にマスの数（＝面積）を集計
ans = [0]*(n+1)
for x in range(mx):
    for y in range(mx):
        ans[t[x][y]] += 1

for k in range(1, n+1):
    print(ans[k])

# 2次元imos法
# ひとまず解き方を暗記するのがよさそう。