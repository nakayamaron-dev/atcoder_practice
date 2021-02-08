#!/usr/bin/env python3
n, m = map(int,input().split())
a = list(map(int, input().split()))

a.append(0)
a.append(n+1)
a.sort()
blanks = []
ans = 0
k = n

for i in range(len(a) - 1):
    blank = a[i+1] - a[i] - 1
    if blank > 0:
        blanks.append(blank)
        k = min(blank, k)

for blank in blanks:
    ans += blank // k

    if blank % k != 0:
        ans += 1

print(ans)

## 概ねできていた。次回チャレンジ
