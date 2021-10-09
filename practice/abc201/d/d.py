#!/usr/bin/env python3
def main():
    H, W = map(int, input().split())
    g = []
    INF = float("inf")

    for _ in range(H):
        a = input()
        r = [1 if char == "+" else -1 for char in a]
        g.append(r)

    # 高橋くんの手番でゲームを開始して、両者が最適な行動をとった際の最終的な点数
    dp_first = [[0]*W for _ in range(H)]
    # 青木くんの手番でゲームを開始して、両者が最適な行動をとった際の最終的な点数
    dp_second = [[0]*W for _ in range(H)]

    for row in reversed(range(H)):
        for col in reversed(range(W)):
            if row == H - 1 and col == W - 1:
                # 右下が-infやinf点になるのを防ぐため
                continue

            # 先行
            s1, s2 = -INF, -INF  # 点数の最大化が目的なので、負の無限大で初期化
            if row + 1 < H:
                s1 = dp_second[row+1][col] + g[row+1][col]
            if col + 1 < W:
                s2 = dp_second[row][col+1] + g[row][col+1]

            dp_first[row][col] = max(s1, s2)

            # 後攻
            s1, s2 = INF, INF  # 点数の最小化が目的なので、正の無限大で初期化
            if row + 1 < H:
                s1 = dp_first[row+1][col] - g[row+1][col]
            if col + 1 < W:
                s2 = dp_first[row][col+1] - g[row][col+1]

            dp_second[row][col] = min(s1, s2)

    # 勝敗判定
    x = dp_first[0][0]
    if x == 0:
        return "Draw"
    elif x > 0:
        return "Takahashi"
    else:
        return "Aoki"


print(main())

# ゲームDP
# 移動先の点数がどちらも確定しているマスの勝敗も確定する。
# 一番右下のマスの点数が0点に確定している(動けないから)
