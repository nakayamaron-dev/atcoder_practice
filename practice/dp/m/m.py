#!/usr/bin/env python3
N, K = map(int,input().split())
A = list(map(int, input().split()))

# dp[i][j]: i番目までの子供たちにj個の飴を配る場合の数
