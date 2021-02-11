#!/usr/bin/env python3
X, Y, A, B = list(map(int, input().split()))

# 経験値がBを超えるまでカコモンジム、その後はAtCoderジムにかよう。
power = X
exp = 0

while (A-1)*power < B and A * power < Y:
    power *= A
    exp += 1 

exp += (Y - power - 1) // B
print(exp)

## Y未満の経験値を求めることに注意。