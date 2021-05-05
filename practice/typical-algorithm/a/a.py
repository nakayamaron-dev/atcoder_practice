#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))

    minval = 0
    maxval = N

    # 二分探索
    while abs(maxval-minval) > 1:
        mid = (minval+maxval) // 2
        if A[mid] >= K:
            maxval = mid
        else:
            minval = mid
    
    if maxval == N:
        return -1
    else:
        return maxval

print(main())

# 二分探索の練習問題
