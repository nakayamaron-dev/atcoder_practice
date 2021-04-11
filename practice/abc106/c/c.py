#!/usr/bin/env python3
S = input()
K = int(input())

cnt = 0
for s in S:
    if s == "1":
        cnt += 1
        if K == cnt:
            print(s)
            exit()
    else:
        print(s)
        exit()

# self AC
