#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0

    for i in range(N):
        ans += abs(A[i] - B[i])
    
    return ans

print(main())