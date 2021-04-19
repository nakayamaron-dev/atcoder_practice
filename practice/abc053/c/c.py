#!/usr/bin/env python3
def main():
    X = int(input())
    ans = 2*(X // 11)

    if X - 11*(ans//2) == 0:
        return ans
    elif X - 11*(ans//2) <= 6:
        return ans + 1
    else:
        return ans + 2

print(main())

# self AC
        