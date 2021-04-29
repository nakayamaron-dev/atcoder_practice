#!/usr/bin/env python3

def solve():
    N = int(input())
    S = set(input() for i in range(N))

    for s in S:
        if "!" + s in S:
            return s

    return "satisfiable"

print(solve())

## self AC
