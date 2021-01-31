#!/usr/bin/env python3
n = int(input())

# 鳩の巣原理
def check(n):
    num = 0
    for i in range(1, n+1):
        num = 10*num + 7
        num = num % n

        if num == 0:
            return i
        else:
            continue
    return -1

print(check(n))