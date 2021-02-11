#!/usr/bin/env python3
n, w = map(int,input().split())

arr = []
for i in range(n):
    #上から順番に代入していく
    s, t, p = map(int, input().split())
    arr.append([s, p])
    arr.append([t, p*(-1)])

arr.sort()

def main():
    water = 0
    for i in arr:
        water += i[1]
        if water > w:
            return 'No'

    return 'Yes'

print(main())

## 毎秒あたりの水の量を求めていくとTLEになることに注意。

