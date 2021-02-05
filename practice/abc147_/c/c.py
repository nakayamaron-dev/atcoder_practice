#!/usr/bin/env python3
import itertools

n = int(input())
XY = []

for i in range(n):
    Ai = int(input())
    xy = [list(map(int, input().split())) for l in range(Ai)]
    XY.append(xy)

# 2**n通り全探索して矛盾がなく、正直者が最大となる組み合わせを選ぶ。
ans = 0
for kind in itertools.product(range(2), repeat=n):
    cnt = sum(kind)
    for i, ki in enumerate(kind):
        if ki == 0:
            continue
        for x, y in XY[i]:
            if kind[x - 1] != y:
                cnt = 0
                break
        else:
            continue
        break

    if ans < cnt:
        ans = cnt

print(ans)

## AC
