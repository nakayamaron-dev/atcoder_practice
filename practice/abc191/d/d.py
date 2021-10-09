#!/usr/bin/env python3
import math
from decimal import Decimal


def main():
    X, Y, R = map(Decimal, input().split())
    ans = 0

    right = math.floor(X + R)
    left = math.ceil(X - R)

    for i in range(left, right+1):
        p = (R**2 - (X-i)**2).sqrt()
        top = math.floor(Y + p)
        botm = math.ceil(Y - p)
        ans += (top - botm) + 1

    return ans


print(main())

# self AC
# 数学の問題
