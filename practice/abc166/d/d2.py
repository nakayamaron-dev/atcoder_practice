#!/usr/bin/env python3
def main():
    X = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == X:
                return [a, b]

print(*main())

# cnt**5 - (cnt-1)**5 > 10**9となるのはcnt = 120であるので、120以下を探索すればよい。
