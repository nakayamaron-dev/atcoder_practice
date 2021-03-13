#!/usr/bin/env python3
N = int(input())
S = input()
prev = ""
ans = []
for i in range(len(S)):
    if S[i] != prev:
        ans.append(S[i])
    prev = S[i]

print(len(ans))

## self AC
