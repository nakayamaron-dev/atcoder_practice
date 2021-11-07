#!/usr/bin/env python3
def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    t = 0

    for a, b in AB:
        t += a / b

    t /= 2
    ans = 0

    for i in range(N):
        a, b = AB[i][0], AB[i][1]
        t -= a / b
        ans += a

        if t < 0:
            ans += t * b
            break

    return ans


print(main())
