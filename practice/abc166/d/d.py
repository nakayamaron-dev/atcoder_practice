#!/usr/bin/env python3
X = int(input())

# Aの範囲は-118 <= A <= 119
# Bの範囲は-119 <= B <= 118

for a in range(-118, 120):
    for b in range(-119, a):
        if a**5 - b**5 == X:
            print(a, b)
            exit() 

# not self AC
# 全探索範囲を決めれれば簡単
