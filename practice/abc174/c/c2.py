#!/usr/bin/env python3
# 方針
# 鳩の巣原理を用いる。：http://www.mathlion.jp/article/ar129.html

K = int(input())

def main():
    num = 0
    for i in range(1, K+1):
        num = 10*num + 7
        num = num % K

        if num == 0:
            return i
    return -1

print(main())

## not self AC
