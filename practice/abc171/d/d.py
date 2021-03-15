#!/usr/bin/env python3
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cnt = Counter(A)
ans = sum(A)

for _ in range(Q):
    b, c = map(int,input().split())
    b_cnt = cnt.get(b, 0)
    c_cnt = cnt.get(c, 0)

    if b_cnt != 0:
        ans += (c-b) * b_cnt

        if c_cnt != 0:
            cnt[c] += b_cnt
        else:
            cnt[c] = b_cnt
        
        cnt.pop(b)

    print(ans)

## self AC
