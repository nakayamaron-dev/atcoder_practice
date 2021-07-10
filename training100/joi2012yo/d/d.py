#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    days, Pasta = [], []

    for _ in range(K):
        D, P = map(int,input().split())
        days.append(D)
        Pasta.append(P)

    # dp[i][j]: i日目にjのパスタを選んだ場合の組み合わせ総数
    dp = [[0]*3 for _ in range(N)]

    for i in range(N):
        if i in days:
            