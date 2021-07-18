#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [int(input()) for _ in range(Q)]
    A.sort()

    for b in B:
        idx = bisect_left(A, b)
        
        if idx == 0:
            ans = abs(A[idx] - b)
        elif idx == N:
            ans = abs(A[idx-1] - b)
        else:
            ans = min(abs(A[idx-1] - b), abs(A[idx] - b))
        
        print(ans)

main()
