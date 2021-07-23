#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    MOD = 10**9 + 7

    if N == 1:
        return K % MOD
    
    if N == 2:
        return (K * (K-1)) % MOD
    
    return (K * (K-1) * pow(K-2, N-2, MOD)) % MOD

print(main())