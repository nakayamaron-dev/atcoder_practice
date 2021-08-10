#!/usr/bin/env python3
def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    l, r = [0], [0]

    for i in range(N):

        # l[i]: A1 ~ Ai-1の最大公約数
        l.append(get_gcd(l[i], A[i]))

        # r[i]: Ai ~ Anの最大公約数
        r.append(get_gcd(r[i], A[N-1-i]))
    
    r = r[::-1]
    for i in range(N):
        ans.append(get_gcd(l[i], r[i+1]))
    
    return max(ans)

print(main())

# 最大公約数の計算は順不同
# 最大公約数計算＋累積の考え方で計算量削減