#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
for i in range(1,N):
    ans += A[i//2]

print(ans)

## not self AC
## 気がつけば簡単にできる。