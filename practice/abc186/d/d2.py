#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    asum = sum(A)
    ans = 0

    for i in range(N):
        asum -= A[i]
        ans += asum - A[i] * (N-(i+1))
    
    return ans

print(main())

# not self AC
# 式変形が苦手。
