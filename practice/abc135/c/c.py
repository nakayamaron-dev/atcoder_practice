#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(len(B)):
    if B[i] > A[i]:
        B[i] -= A[i]
        ans += A[i]
    else:
        ans += B[i]
        B[i] = 0
    
    if B[i] < A[i+1]:
        ans += B[i]
        A[i+1] -= B[i]
    else:
        ans += A[i+1]
        A[i+1] = 0
    
print(ans)

## not self AC
