#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    mxg = mxp = cur = step = 0

    for i in range(N):
        # 累積
        step += A[i]

        # i番目の動作の最大値(累積和が最大値を更新したら)
        mxp = max(mxp, step)

        # i番目の動作までの最大得点
        mxg = max(mxg, cur+mxp)

        # i番目の動作終了時の得点
        cur += step

    return mxg


print(main())
