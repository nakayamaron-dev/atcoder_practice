#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = sorted(A)
    tgt = AA[-2]

    return A.index(tgt) + 1

print(main())