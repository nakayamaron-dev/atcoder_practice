#!/usr/bin/env python3
N, Q = map(int,input().split())
S = input()

C = [0]
for i in range(1, N):
    if S[i-1:i-1+2] == "AC":
        C.append(C[-1] + 1)
    else:
        C.append(C[-1])

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(C[r] - C[l])

# not self AC