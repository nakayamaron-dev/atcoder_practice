#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    ans = 0

    for itm_b in B:
        idx_a = bisect_left(A, itm_b)
        idx_c = bisect_right(C, itm_b)
    
        ans += idx_a * (N - idx_c)
    
    return ans

print(main())
