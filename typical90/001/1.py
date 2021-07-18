#!/usr/bin/env python3
def main():
    N, L = map(int,input().split())
    K = int(input())
    A = list(map(int, input().split()))
    A += [L] # 終点も一つの切り目として加えておく。

    #二分探索：最小の長さがXとなる組み合わせが存在するかどうか
    l, r = 1, L+1

    while r-l > 1:
        mid = (l+r) // 2
        cnt = 0
        start = 0

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
