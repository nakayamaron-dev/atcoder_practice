#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Max = 10 ** 6 + 1
    cnt = [0] * Max

    for i in A:
        # 同じ値がある場合は、後で判別できるように∞を代入しておく。
        if cnt[i] != 0:
            cnt[i] = float("inf")
            continue

        # iの倍数の箇所をインクリメントする。
        for j in range(i, Max, i):
            cnt[j] += 1
    
    ans = 0
    for i in A:
        # 1以上になる箇所はAの中に割り切れる数が含まれることを示している。
        if cnt[i] == 1:
            ans += 1
    
    return ans

print(main())


