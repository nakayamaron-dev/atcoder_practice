#!/usr/bin/env python3
def get_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    l = [0]
    r = [0]

    for i in range(n):
        # l[i]: a1, a2,..., ai-1の最大公約数
        l.append(get_gcd(l[i], a[i]))

        # r[i]: ai, ai+1,..., anの最大公約数
        r.append(get_gcd(r[i], a[n-1-i]))
    
    r = r[::-1]
    for i in range(n):
        ans.append(get_gcd(l[i], r[i+1]))

    return max(ans)

print(main())

# not self AC
# 最大公約数の計算が順不同であることを利用し、前後両方から累積最大公約数をリストに格納しておく技が思いつかない。
# 後ろからのリストを逆順にソートすることも忘れずに。
