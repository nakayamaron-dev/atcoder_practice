#!/usr/bin/env python3
N, M = map(int,input().split())
AB = [list(map(int, input().split())) for l in range(N)]
AB.sort()
ans = 0
drink = 0

for ab in AB:
    cnt = 0
    while drink < M and cnt < ab[1]:
        ans += ab[0]
        cnt += 1
        drink += 1
    
    if drink == M:
        print(ans)
        exit()

# self AC
