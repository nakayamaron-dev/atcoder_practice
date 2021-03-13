#!/usr/bin/env python3
N, K = map(int,input().split())

mod = N % K
ans = min(abs(mod), abs(mod-K))
print(ans)

## self AC