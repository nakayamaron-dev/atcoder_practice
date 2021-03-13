#!/usr/bin/env python3
# 数字を桁ごとにリスト化
def splitdigit(num):
    return list(map(int, str(num)))

N, M = map(int,input().split())
SC = [list(map(int, input().split())) for l in range(M)]

def main():
    maxval = 10**N
    minval = 10**(N-1)

    if N == 1:
        minval = 0

    for i in range(minval, maxval):
        digits = splitdigit(i)

        for sc in SC:
            if digits[sc[0]-1] != sc[1]:
                break
        else:
            return i
            
    return -1

print(main())

## self AC
