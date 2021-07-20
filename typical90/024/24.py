#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dim = 0

    for i in range(N):
        dim += abs(A[i] - B[i])
    
    if dim > K:
        return "No"
    else:
        if (dim - K) % 2 == 0:
            return "Yes"
        else:
            return "No"
    
print(main())