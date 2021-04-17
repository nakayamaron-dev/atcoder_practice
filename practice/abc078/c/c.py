#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    time = 1900*M + (N-M)*100
    prob = 0.5 ** M

    return int(time // prob)

print(main())

# self AC
