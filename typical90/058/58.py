#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    MAX = 10**5

    dp = [False] * MAX
    dp[N] = True
    cache = [N]

    # 鳩ノ巣原理より、100000回処理すればいつかループする。
    for i in range(MAX):
        N += sum(int(c) for c in str(N))
        N %= MAX
        if dp[N]: break

        dp[N] = True
        cache.append(N)

    if K < len(cache):
        return cache[K]
    
    start = 0
    for i in range(len(cache)):
        if N == cache[i]:
            start = i
            break
    
    #loopの要素数を計算する。
    loop = len(cache) - start

    if loop == 0: return N
    
    K -= start
    K %= loop
    K += start

    return cache[K]

print(main())