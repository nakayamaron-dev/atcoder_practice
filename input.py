#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(N)]
    L = [list(map(int, input().split())) for _ in range(N)]
    MOD = 10**9 + 7
    INF = float("inf")
    ans = 0

print(main())