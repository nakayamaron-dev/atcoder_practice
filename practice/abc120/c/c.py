#!/usr/bin/env python3
S = input()
zero, one = 0, 0

for s in S:
    if s == "0":
        zero += 1
    else:
        one += 1

print(min(zero, one)*2)

# self AC
