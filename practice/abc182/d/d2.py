#!/usr/bin/env python3
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    all_cum = 0
    maxv = 0
    a_cum = 0
    for i in range(n):
        # i番目までの累積和
        a_cum += a[i]
        # i番目までの累積和で最も大きい値
        maxv = max(maxv, a_cum)
        # この段階ではall_cumはi-1番目までに手順の累積和
        ans = max(ans, all_cum + maxv)
        # ここでall_cumはi番目までに手順の累積和
        all_cum += a_cum

    return ans


print(main())
