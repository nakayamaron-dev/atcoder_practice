#!/usr/bin/env python3
A, B = map(int,input().split())
C, D = map(int,input().split())

x = max(A, B)
y = min(C, D)

print(x-y)