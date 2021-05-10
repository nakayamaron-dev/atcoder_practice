#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    R, S, P = map(int,input().split())
    T = input()

    judge = [True] * N
    ans = 0

    # i番目で勝ち & i+k番目が同じ場合i+k番目は勝たない手を出す。
    for i in range(N):
        if i+K < N and T[i] == T[i+K] and judge[i]:
            ans += 0
            judge[i+K] = False
        elif T[i] == "r":
            ans += P
        elif T[i] == "s":
            ans += R
        elif T[i] == "p":
            ans += S
    
    return ans

print(main())

# not self AC
# 貪欲法で解いたが、DPでも解けるらしい。
