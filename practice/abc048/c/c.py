#!/usr/bin/env python3
def main():
    N, X = map(int,input().split())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N-1):
        if A[i] > X:
            ans += A[i] - X
            A[i] = X

        if A[i] + A[i+1] > X:
            ans += A[i] + A[i+1] - X
            A[i+1] = X - A[i]

    return ans

print(main())

#self AC
