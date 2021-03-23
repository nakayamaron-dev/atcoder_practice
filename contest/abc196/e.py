#!/usr/bin/env python3
N = int(input())
AT = [list(map(int, input().split())) for l in range(N)]
Q = int(input())
X = list(map(int, input().split()))

def ft1(x, ai):
    return x+ai
def ft2(x, ai):
    return max(x, ai)
def ft3(x, ai):
    return min(x, ai)
