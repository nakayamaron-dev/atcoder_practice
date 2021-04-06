#!/usr/bin/env python3
import itertools
N = int(input())

def digit_num(num):
    return len(str(num))

digit_num = digit_num(N)
ans = 0

for i in range(3, digit_num+1):
    ptn = itertools.product('357', repeat=i)
    for itm in ptn:
        num = 0
        if len(set(itm)) != 3:
            continue

        for idx, digit in enumerate(itm):
            num += int(digit) * 10**idx
        
        if num <= N:
            ans += 1

print(ans)

# self AC
