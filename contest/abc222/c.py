#!/usr/bin/env python3
def judge(s1, s2):
    if s1 == "G" and s2 == "P":
        return 2
    elif s1 == "G" and s2 == "C":
        return 1
    elif s1 == "C" and s2 == "P":
        return 1
    elif s1 == "C" and s2 == "G":
        return 2
    elif s1 == "P" and s2 == "G":
        return 1
    elif s1 == "P" and s2 == "C":
        return 2
    else:
        return 0


def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(2*N)]
    order = [[x, 0] for x in range(2*N)]

    for j in range(M):
        for i in range(0, len(order), 2):
            w = judge(A[order[i][0]][j], A[order[i+1][0]][j])
            if w == 1:
                order[i][1] -= 1
            elif w == 2:
                order[i+1][1] -= 1

        order = sorted(order, key=lambda x: (x[1], x[0]))

    for o in order:
        print(o[0] + 1)


main()
