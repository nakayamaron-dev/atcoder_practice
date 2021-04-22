#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    avg1 = sum(A) // len(A)
    avg2 = sum(A) // len(A) + 1
    ans1, ans2 = 0, 0

    for a in A:
        ans1 += (a-avg1)**2
        ans2 += (a-avg2)**2

    return min(ans1, ans2)

print(main())

# self AC
