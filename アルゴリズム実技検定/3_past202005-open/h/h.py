#!/usr/bin/env python3
def main():
    n, l = map(int,input().split())
    x = list(map(int, input().split()))
    t1, t2, t3 = map(int,input().split())

    # ハードル情報を管理する配列
    h = [False] * (l+1)
    for itm in x:
        h[itm] = True

    #dp[i]: 座標iで行動を終了するまでの最小所要時間
    dp = [float("inf")] * (l+1)
    dp[0] = 0

    # 順番に求めていく
    for i in range(1, l+1):
        # 行動１
        dp[i] = min(dp[i], dp[i-1] + t1)

        # 行動２
        if i >= 2:
            dp[i] = min(dp[i], dp[i-2] + t1 + t2)
        
        # 行動３
        if i >= 4:
            dp[i] = min(dp[i], dp[i-4] + t1 + 3*t2)
        
        # ハードルがあれば加算
        if h[i]:
            dp[i] += t3
    
    ans = dp[l]

    # 答えは座標lにピッタリ止まるか、座標l-3 ~ l-1からジャンプ中にゴールしたものの中の最小
    for i in [l-3, l-2, l-1]:
        if i >= 0:
            ans = min(ans, dp[i] + t1//2 + t2*(2*(l-i)-1)//2)
    
    return ans

print(main())