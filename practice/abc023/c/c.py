#!/usr/bin/env python3
from collections import Counter
def main():
    R, C, K = map(int,input().split())
    N = int(input())

    ame = []
    row = [0]*R
    col = [0]*C

    for _ in range(N):
        r, c = map(int, input().split())
        row[r-1] += 1
        col[c-1] += 1
        ame.append((r-1, c-1))
    
    rc = Counter(row)
    cc = Counter(col)
    ans = 0

    for k, v in rc.items():
        ans += cc[K-k] * v
    
    for r, c in ame:
        if row[r] + col[c] == K:
            ans -= 1
        if row[r] + col[c] == K+1:
            ans += 1
    
    return ans

print(main())

# not self AC
# 難しいけど良い問題
