#!/usr/bin/env python3
def main():
    N = int(input())
    
    while True:
        N = N // 2 + 1
        if N == 1:
            return "Aoki"
        N //= 2
        if N == 1:
            return "Takahashi"
        N -= 1

print(main())

# not self AC
# 難しい。
