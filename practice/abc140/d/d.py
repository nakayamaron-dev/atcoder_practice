#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    S = input()
    ans = 0

    for i in range(1, N):
        if S[i] == S[i-1]:
            ans += 1
    
    return min(N-1, ans + K*2)

print(main())

# not self AC
# 1回の試行で幸福度は最大2までしか上がらない。
# かつ、全員が同じ方向を向くまで必ず2上がる選び方は存在する。
# よって、K回試行するまでに全員同じ方向を向くか、K回幸福度を2ずつ上げていくかどちらか低い方が答えになる。
