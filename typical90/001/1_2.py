#!/usr/bin/env python3
def main():
    N, L = map(int,input().split())
    K = int(input())
    A = list(map(int, input().split()))
    A += [L]

    # 二分探索
    l, r = 0, L+1
    while r - l > 1:
        mid = (r+l) // 2
        start = 0
        cnt = 0

        for i in range(N+1):
            if A[i] - start >= mid:
                start = A[i]
                cnt += 1
        
        if cnt >= K+1:
            l = mid
        else:
            r = mid
    
    return l

print(main())