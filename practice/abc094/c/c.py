#!/usr/bin/env python3
def main():
    N = int(input())
    X = list(map(int, input().split()))
    X_sr = sorted(X)

    for x in X:
        if x >= X_sr[N // 2]:
            print(X_sr[N // 2 - 1])
        else:
            print(X_sr[N // 2])

main()

# self AC
# 簡単
