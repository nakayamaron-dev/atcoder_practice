#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    l = [[] for _ in range(N)]

    for _ in range(M):
        A, B = map(int,input().split())
        l[A-1].append(B)

    for idx in l[0]:
        if N in l[idx-1]:
            return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

print(main())

# self AC
