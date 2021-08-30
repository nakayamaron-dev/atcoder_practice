#!/usr/bin/env python3
def color_check(color: int, cylinder_i: int) -> None:
    if color in top_colors:
        stack.append((top_colors[color], cylinder_i))
    else:
        top_colors[color] = cylinder_i

    return


N, M = map(int, input().split())
A = []
top_colors = {}  # 各色で最初に一番上に来たボールのインデックス
stack = []  # 捨てることができるインデックスのペア

for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))[::-1]  # pop()で捨てたいので反転
    A.append(a)
    color_check(a[-1], i)

while stack:
    i, j = stack.pop()  # 捨てることができるペアを一つ取り出す。
    for k in [i, j]:
        A[k].pop()  # 筒の一番上を捨てる

        if not A[k]:  # 筒が空になったらメモ更新は不要
            continue

        color_check(A[k][-1], k)

# any()で全て空になっているか判定
if any(A):
    print("No")
else:
    print("Yes")
