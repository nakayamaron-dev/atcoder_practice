#!/usr/bin/env python3

# Aの読む冊数を固定してBを何冊読めるか探索する。
# TLE対策として予めBの累積和配列を用意しておく。
from bisect import bisect_left,bisect_right

def main():
    N, M, K = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    acm_a = [0]
    acm_b = [0]
    ans = 0

    for a in A:
        acm_a.append(acm_a[-1] + a)

    for b in B:
        acm_b.append(acm_b[-1] + b)
    
    for i in range(len(acm_a)):
        time = acm_a[i]
        a = i

        if time <= K:
            b = bisect_right(acm_b, K - time) - 1
            time += acm_b[b]

        if time <= K:
            ans = max(ans, a+b)

    return ans

print(main())

# self AC
