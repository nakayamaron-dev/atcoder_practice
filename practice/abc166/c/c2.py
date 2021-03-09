#!/usr/bin/env python3
N, M = map(int,input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for l in range(M)]

ans = [0]*N

for p1, p2 in AB:
    if H[p1-1] < H[p2-1]:
        ans[p1-1] = 1
    elif H[p1-1] > H[p2-1]:
        ans[p2-1] = 1
    else:
        ans[p1-1] = 1
        ans[p2-1] = 1

print(ans.count(0))

# self AC
