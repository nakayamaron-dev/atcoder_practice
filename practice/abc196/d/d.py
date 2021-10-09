#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 6)

h, w, a, b = map(int, input().split())

used = [[0]*w for _ in range(h)]  # 畳があるか管理

res = 0

# マス(1,1)から(1,w)、(2,1)から(2,w)・・・(h,1)から(h,w)の順にdfs


def dfs(i, j, a, b):
    global res
    if a < 0 or b < 0:  # 畳がa枚以下やb枚以下になれば失敗
        return
    if j == w:      # 右端に来たら次の行へ
        j = 0
        i += 1
    if i == h:      # iがhになれば成功(条件にあう畳の敷き詰め方)
        res += 1
        return
    if used[i][j] == 1:  # 調べるマスに畳があれば次のマスに
        return dfs(i, j+1, a, b)

    used[i][j] = 1
    dfs(i, j+1, a, b-1)    # 半畳 使う場合
    if j+1 < w and used[i][j+1] == 0:  # 横に1畳置く場合
        used[i][j+1] = 1
        dfs(i, j+1, a-1, b)
        used[i][j+1] = 0

    if i+1 < h and used[i+1][j] == 0:  # 縦に1畳置く場合
        used[i+1][j] = 1
        dfs(i, j+1, a-1, b)
        used[i+1][j] = 0

    used[i][j] = 0  # 元に戻す
    return res


print(dfs(0, 0, a, b))

# not self AC
