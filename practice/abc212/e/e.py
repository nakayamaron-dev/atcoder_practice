#!/usr/bin/env python3
def main():
    N, M, K = map(int,input().split())
    g = [[i] for i in range(N+1)]
    MOD = 998244353

    for _ in range(M):
        U, V = map(int,input().split())
        U, V = U-1, V-1
        g[U].append(V)
        g[V].append(U)
    
    dp = [[0]*N for _ in range(K+1)]
    dp[0][0] = 1

    for k in range(1, K+1):
        all_sum = sum(dp[k-1])
        for i in range(N):
            dp[k][i] = all_sum
            for j in g[i]:
                dp[k][i] -= dp[k-1][j]
            
            dp[k][i] %= MOD
    
    return dp[K][0]

print(main())