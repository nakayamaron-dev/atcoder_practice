#!/usr/bin/env python3
S = input()

A = [0] * 2019
A[0] = 1

answer, x, p = 0, 0, 1
for itm in S[::-1]:
    x = (x + int(itm) * p) % 2019
    p = (p * 10) % 2019
    answer += A[x]
    A[x] += 1
print(answer)

# not self AC
