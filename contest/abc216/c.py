import math


def main():
    N = int(input())
    ans = ""
    t = 1

    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans += "B"
        else:
            N -= 1
            ans += "A"

    return ans[::-1]


print(main())
