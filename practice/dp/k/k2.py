#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))

    #dp[i]: 石の個数がi個のとき直後の手番の人が勝てるかどうか。
    dp = [False] * (K+1)

    for i in range(1, K+1):
        # a個の石をとってもまだ石が残っている & 直後の手番の人が勝てない選択が一つでも残っている場合はそれを選ぶ。
        for a in A:
            if i-a >= 0 and dp[i-a] == False:
                dp[i] = True
                break
    
    if dp[-1] == True:
        return "First"
    else:
        return "Second"

print(main())

# not self AC
# 基本的な問題
