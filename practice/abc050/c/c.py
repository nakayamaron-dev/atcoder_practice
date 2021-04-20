#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mod = 10**9 +7

    if N % 2 == 1:
        if A[0] != 0:
            return 0
        
        for i in range(1, N, 2):
            if A[i] != i+1 or A[i+1] != i+1:
                return 0
        
        return 2 ** ((N-1)//2) % mod
    else:
        for i in range(0, N, 2):
            if A[i] != i+1 or A[i+1] != i+1:
                return 0
        
        return 2 ** (N//2) % mod

print(main())
    
# self AC    
