#!/usr/bin/env python3
from collections import Counter
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    cnt = sorted(Counter(A).items(), key=lambda x:x[1])
    ans = 0

    for i in range(len(cnt)-K):
        ans += cnt[i][1]
    
    return ans

print(main())

# self AC
