#!/usr/bin/env python3
N, M = map(int,input().split())
X = list(map(int, input().split()))
X.sort()
dims = []

if N >= M:
    print(0)
else:
    for i in range(M-1):
        dims.append(X[i+1] - X[i])

    dims.sort(reverse=True)
    ans = sum(dims[N-1:])
    print(ans)
    
# not self AC
