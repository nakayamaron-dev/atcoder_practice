#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for key, val in Counter(A).items():
        key = int(key)
        if key > val:
            ans += val
        elif key < val:
            ans += val - key
    
    return ans

print(main())

# self AC
