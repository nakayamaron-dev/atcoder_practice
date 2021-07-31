#!/usr/bin/env python3
def main():
    N = int(input())

    first, second = [0], [0]
    for _ in range(N):
        c, p = map(int,input().split())

        if c == 1:
            first.append(first[-1] + p)
            second.append(second[-1])
        else:
            second.append(second[-1] + p)
            first.append(first[-1])

    Q = int(input())
    for _ in range(Q):
        l, r = map(int,input().split())

        tgt1 = first[r] - first[l-1]
        tgt2 = second[r] - second[l-1]

        print(tgt1, tgt2)

main()