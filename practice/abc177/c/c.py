#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
Sum = sum(a)
ans = 0

for idx, itm in enumerate(a):
    Sum -= a[idx]
    ans += itm*Sum

print(ans % (10**9 + 7))

## AC