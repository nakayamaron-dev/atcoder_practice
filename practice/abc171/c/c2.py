#!/usr/bin/env python3
# 方針
# 桁数は26**n
# 数字 → アルファベット変換
n = int(input())

def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

print(num2alpha(n).lower())

# not self AC