#!/usr/bin/env python3
n = int(input())
cnt = dict()
 
ans = 0
for _ in range(n):
  s = "".join(sorted(list(input())))
  ans += cnt.get(s, 0)
  cnt[s] = cnt.get(s, 0) + 1
 
print(ans)

## dictのgetの使いかたを理解した。