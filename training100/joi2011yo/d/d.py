#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # dp[i][j]: 左からi番目までの数式で答えがjになる組み合わせが何パターンあるか。
    dp = [[0]* 21 for _ in range(N)]
    dp[0][A[0]] = 1

    for i in range(1, N-1):
        tmp = A[i]
        for j in range(21):
            cnt = dp[i-1][j]

            if cnt != 0:
                if j + tmp <= 20:
                    dp[i][j+tmp] += cnt
                
                if j - tmp >= 0:
                    dp[i][j-tmp] += cnt
    
    return dp[N-2][A[-1]]

print(main())
