#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    mod = 10**9 + 7
    arr = [i for i in range(N+1)]
    ans = 0
    acm_l, acm_r = [], []

    for i in range(len(arr)):
        if i == 0:
            acm_l.append(arr[i])
            acm_r.append(arr[N-i])
        else:
            acm_l.append(acm_l[i-1] + arr[i])
            acm_r.append(acm_r[i-1] + arr[N-i])

    for i in range(K, N+2):
        ans += acm_r[i-1] - acm_l[i-1] + 1
        ans %= mod
    
    return ans

print(main())

# 10**100は巨大な数字なため、選ぶ個数が異なるとその和も必ずことなる。
# K, K+1...N個それぞれ選ぶときの個数を足していけば良い。
# ポイントは例えばM個選ぶとき、和の最小は小さい方からM個選んだ場合、最大は大きい方からM個選んだ場合である。
# その間にある数は組み合わせで必ず作ることができるので最大と最小の差を計算すればO(1)で計算できる。