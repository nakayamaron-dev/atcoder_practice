#!/usr/bin/env python3
import math
def main():
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    dim = []
    k = N

    for i in range(M+1):
        blank = A[i+1] - A[i] - 1
        if blank > 0:
            dim.append(blank)
            k = min(k, blank)
    
    ans = 0
    for itm in dim:
        ans += int(math.ceil(itm/k))
    
    return ans

print(main())

# self AC
