#!/usr/bin/env python3
N, K = map(int,input().split())
A = list(map(int, input().split()))
A.sort()

# dp[i]: 石の個数がi個のとき直後の手番の人が勝てるか。
dp = [False] * (K+1)

for i in range(1, K+1):
    for a in A:
        # a個の石をとってもまだ石が残っていて、石がi-a個のとき、直後の手番の人が勝てない場合が１パターンでもあればそれを選べば良い。
        if i-a >= 0 and dp[i-a] == False:
            dp[i] = 1
            break

if dp[-1] == True:
    print("First")
else:
    print("Second")

## not self AC