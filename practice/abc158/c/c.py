#!/usr/bin/env python3
a, b = map(int,input().split())
tax_8 = 0.08
tax_10 = 0.1

# 最大で1009円までなので小さい方から計算していく。
def main():
    for i in range(1, 1010):
        if int(i * tax_8) == a and int(i * tax_10) == b:
            return i
    return -1

print(main())

## AC
