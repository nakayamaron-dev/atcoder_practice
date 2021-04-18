#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    s = 0
    a = sum(A)
    ans = 10**10

    for i in range(N-1):
        s += A[i]
        a -= A[i]
        ans = min(abs(s-a), ans)
    
    return ans

print(main())

# self AC
