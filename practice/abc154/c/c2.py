#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

if len(A) == len(set(A)):
    print("YES")
else:
    print("NO")

## self AC