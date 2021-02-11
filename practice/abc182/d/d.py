#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

mxg = mxp = cur = step = 0

for i in a:
    step += i
    mxp = max(mxp, step)
    mxg = max(mxg, cur+mxp)
    cur += step

print(mxg)

# 動作iの合計の座標の変化
# 動作iを座標0で始めた場合の、開始から終了までの座標の最大値
# であれば制限時間内で求められる。
