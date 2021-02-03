#!/usr/bin/env python3
import collections

n = int(input())
s = [str(input()) for _ in range(n)]

c = collections.Counter(s)
c = sorted(c.items(), key=lambda x:x[1], reverse=True)

max_num = 0
ans = []

for idx, itm in enumerate(c):
    if idx == 0:
        max_num = itm[1]
        ans.append(itm[0])
    else:
        if itm[1] >= max_num:
            ans.append(itm[0])

ans = sorted(ans)
for itm in ans:
    print(itm)

## AC
