#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    MOD = 10**4
    menu = [0] * N
    for i in range(K):
        a, b = map(int, input().split())
        menu[a - 1] = b
    
    # 0:決まってない、1:トマトソース、2:クリームソース、3:バジルソース
    # dp[i][j][k]: i-1日目にk、i-2日目にjを選んだ場合i日目までのパスタの選び方の総数。
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]

    dp[0][0][0] = 1
    # 日付
    for n in range(N):
        # 1日前のパスタ
        for i in range(4):
            # 2日前のパスタ
            for j in range(4):
                # 当日のパスタ
                for k in range(1, 4):
                    if menu[n] != 0 and menu[n] != k: # パスタが指定されているのにkが違えばスキップ
                        continue
                    if not (k == i == j): # 三日連続ではない場合
                        dp[n+1][k][i] += dp[n][i][j]
                        dp[n+1][k][i] %= MOD

    ans = 0
    for i in range(1, 4): # 最終日、ダミー以外の全ての状態の分を足す
        for j in range(1, 4):
            ans += dp[-1][i][j]
            ans %= MOD

    return ans

print(main())
            