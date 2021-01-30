#!/usr/bin/env python3
X, K, D = map(int, input().split())
X = abs(X)

count = X // D
mod = X % D

if count >= K:
    print(X - K*D)
else:
    if (K - count) % 2 == 1:
        print(abs(X - D*(count + 1)))
    else:
        print(abs(mod))

## AC
