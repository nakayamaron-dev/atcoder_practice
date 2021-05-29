#!/usr/bin/env python3
from collections import Counter

def main():
    N = int(input())
    S = ["".join(sorted(input())) for _ in range(N)]
    cnt = Counter(S)
    
    ans = 0
    for val in cnt.values():
        ans += val * (val-1) // 2
    
    return ans

print(main())