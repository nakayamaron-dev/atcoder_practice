#!/usr/bin/env python3
def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    S.sort()

    if sum(S) % 10 != 0:
        return sum(S)

    for s in S:
        if s % 10 != 0:
            return sum(S) - s
    return 0

print(main())

# self AC
