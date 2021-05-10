#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0

    # 桁毎に０と１の個数を計算し、その個数の積 x 2^桁数を加算していけば良い。
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        
        ans += cnt * (N-cnt) * pow(2, i, mod)
        ans %= mod
    
    return ans

print(main())

# not self AC
# bit演算は桁毎に独立している性質をうまく使い、計算量を工夫する。
# pythonだとTLEになるので、PyPyを使う。
