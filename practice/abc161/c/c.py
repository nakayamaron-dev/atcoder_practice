#!/usr/bin/env python3
n, k = map(int,input().split())

num = n - k * ((n // k))

if num > abs(k - num):
    print(abs(k - num))
else:
    print(num)

## AC
