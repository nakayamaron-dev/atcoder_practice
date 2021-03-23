#!/usr/bin/env python3
N = input()

if "." not in N:
    print(N)
else:
    idx = N.index(".")
    print(N[0:idx])
