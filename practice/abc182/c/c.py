#!/usr/bin/env python3
N = int(input())
digitArray = list(map(int, str(N)))
digitSum = sum(list(map(int, str(N))))

def mod3(num):
    return num % 3

# 全桁の和が3の倍数の場合はそのまま0
# 全桁の和を3で割ると余りが1の場合
# それぞれの桁を3で割り、余りが1の数字が存在すればその数を消す。存在しない場合、余りが2の数が最低2つあるはずなので2つ消す。
# 2つ消す際、Nが2桁であれば消滅するため、-1
# 全桁の和を3で割ると余りが2の場合も余り1のときと同様

if digitSum % 3 == 0:
    print('0')
elif digitSum % 3 == 1:
    if 1 in map(mod3, digitArray):
        if len(digitArray) <= 1:
            print('-1')
        else:
            print('1')
    else:
        if len(digitArray) <= 2:
            print('-1')
        else:
            print('2')
else:
    if 2 in map(mod3, digitArray):
        if len(digitArray) <= 1:
            print('-1')
        else:
            print('1')
    else:
        if len(digitArray) <= 2:
            print('-1')
        else:
            print('2')
