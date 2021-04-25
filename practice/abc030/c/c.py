#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
def main():
    N, M = map(int,input().split())
    X, Y = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans, a_cnt, b_cnt, time = 0, 0, 0, 0

    while time <= A[-1] and time <= B[-1]:
        if a_cnt >= len(A) or b_cnt >= len(B): break

        time += X + (A[a_cnt] - time)
        b_cnt = bisect_left(B, time)

        if a_cnt >= len(A) or b_cnt >= len(B): break

        time += Y + (B[b_cnt] - time)
        a_cnt = bisect_left(A, time)
        ans += 1
    
    return ans

print(main())

# self AC
