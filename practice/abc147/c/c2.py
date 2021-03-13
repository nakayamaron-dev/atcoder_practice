#!/usr/bin/env python3
def iter_product(n: int):
    import itertools
    return itertools.product(range(2), repeat=n)

N = int(input())
XY = []

for i in range(N):
    Ai = int(input())
    xy = [list(map(int, input().split())) for l in range(Ai)]
    XY.append(xy)

ans = 0
for ptn in iter_product(N):
    flag = True
    for idx, itm in enumerate(XY):
        if ptn[idx] == 1:
            for comment in itm:
                if ptn[comment[0]-1] != comment[1]:
                    flag = False
                    break
        else:
            for comment in itm:
                if ptn[comment[0]-1] == comment[1]:
                    flag = False
                    break
    if flag:
        ans = max(ans, sum(ptn))

print(ans)

## not self AC
