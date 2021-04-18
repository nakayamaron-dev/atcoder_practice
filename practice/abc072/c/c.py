#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = Counter(A)

    if N == 1:
        return 1
    
    if N == 2:
        if abs(A[0] - A[1]) <= 1:
            return 2
        else:
            return 1

    ans = 0
    for i in range(N-2):
        ans = max(counter.get(i, 0) + counter.get(i+1, 0) + counter.get(i+2, 0), ans)
    
    return ans

print(main())

# self AC
