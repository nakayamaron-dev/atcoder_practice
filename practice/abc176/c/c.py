#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

max_val = a[0]
anss = []

for itm in a:
    # 最大値の更新
    if itm > max_val:
        max_val = itm

    anss.append(max_val - itm)

print(sum(anss))

## AC
