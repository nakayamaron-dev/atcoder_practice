#!/usr/bin/env python3
# 二分探索すればいけそう。

def main():
    A, B, X = map(int,input().split())
    l = 0
    r = 10**9 + 1
    
    while r - l > 1:
        mid = (r+l) // 2
        cost = A * mid + B * len(str(mid))

        if cost > X:
            r = mid
        else:
            l = mid

    return l

print(main())

# self AC
