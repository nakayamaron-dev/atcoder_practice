#!/usr/bin/env python3

a, b = map(int, input().split())
c, d = map(int, input().split())

r = c - a
c = d - b

if (r, c) == (0, 0):
    ans = 0
elif r == c or r == -c:
    ans = 1
elif abs(r) + abs(c) <= 3:
    ans = 1
elif (r + c) % 2 == 0:
    ans = 2
elif abs(r) + abs(c) <= 6:
    ans = 2
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    ans = 2
else:
    ans = 3

print(ans)

## self AC