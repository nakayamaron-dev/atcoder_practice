#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))

    ans = sum(A) * K

    for i in range(N):
        if i <= K-2:
            ans -= A[i] * (K-i-1)
        
        if (N-i) <= K-1:
            ans -= A[i] * (K - N + i)
        
    return ans

print(main())

# self AC
