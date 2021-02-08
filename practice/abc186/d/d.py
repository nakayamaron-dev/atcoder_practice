#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0

asum = sum(a)

for i in range(n):
    asum -= a[i]
    ans += asum - a[i]*(n - i -1)

print(ans)

 ## 式変形をして2重ループを回避する。