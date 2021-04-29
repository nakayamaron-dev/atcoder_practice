#!/usr/bin/env python3

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)
 
def solve():
    N = int(input())
    ans = 0

    for i in range(1, N+1):
        if ("7" not in str(i)) and ("7" not in base10int(i, 8)):
            ans += 1

    return ans

print(solve())

# self AC
# 進数変換できればとても簡単