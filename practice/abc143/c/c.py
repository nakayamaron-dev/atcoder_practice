#!/usr/bin/env python3
n = int(input())
s = str(input())

ans = 0
for idx, itm in enumerate(s):
    if idx != 0:
        if s[idx - 1] != s[idx]:
            ans += 1

print(ans + 1)

## AC
