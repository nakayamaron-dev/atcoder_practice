#!/usr/bin/env python3
# 方針
# N, Mが12までなので、おそらく2**12の全探索
# シフト演算にチャレンジ
N, M, X = map(int,input().split())
CA = [list(map(int, input().split())) for l in range(N)]

def Sum(n1, n2):
    return n1 + n2

def main():
    min_cost = 10**9
    for i in range(1, 2**N):
        arr = []
        for n in range(N):
            if (i>>n)&1:
                if len(arr) == 0:
                    arr = CA[n]
                else:
                    arr = list(map(Sum, arr, CA[n]))
        
        if min(arr[1:]) >= X:
            if arr[0] < min_cost:
                min_cost = arr[0]
    
    if min_cost == 10**9:
        return -1
    else:
        return min_cost

print(main())

## self AC