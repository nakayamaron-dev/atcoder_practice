#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 到着順にソート(フレンドリーさが大きい順番に到着すること最適)
    A.sort(reverse=True)

    ans = 0
    for i in range(1, N):
        ans += A[i//2]

    return ans

print(main())

# 2番目の要素から2分木になる。
# 最適に割り込んでいくと、最大の要素は1回、それ以降は2回ずつ足されることになる。
