#!/usr/bin/env python3
def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    dp = [float('inf')] * N

    for i in range(N*2):
        #Takahashiからもらうか、隣の人からもらうか早い方を採用する。
        dp[i%N] = min(T[i%N], dp[i%N - 1] + S[i%N - 1])
    
    for ans in dp:
        print(ans)

main()