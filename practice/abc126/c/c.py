#!/usr/bin/env python3
N, K = map(int,input().split())
ans = 0

for n in range(1, N+1):
    cnt = 0
    while n <= K-1:
        cnt += 1
        n *= 2
    
    ans += 0.5**cnt / N

print(ans)

# not self AC
