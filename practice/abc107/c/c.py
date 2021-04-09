#!/usr/bin/env python3
N, K = map(int,input().split())
X = list(map(int, input().split()))

ans = 10**9
for i in range(N-K+1):
    if X[i] * X[i+K-1] < 0:
        dist1 = 2*X[i+K-1] - X[i]
        dist2 = X[i+K-1] - 2*X[i]
        dist = min(dist1, dist2)
    else:
        dist = max(abs(X[i]), abs(X[i+K-1]))
    
    ans = min(ans, dist)

print(ans)

# self AC
