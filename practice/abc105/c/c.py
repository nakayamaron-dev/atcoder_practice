#!/usr/bin/env python3
N = int(input())

ans = ""
while N != 0:
    ans = str(N%2) + ans
    N = -(N//2)

if ans == "":
    print(0)
else:
    print(ans)

# not self AC