#!/usr/bin/env python3
N = int(input())
cache = dict()
ans = 0

for i in range(N):
    s = "".join(sorted(list(input())))
    ans += cache.get(s, 0)
    cache[s] = cache.get(s, 0) + 1

print(ans)

## not self AC
