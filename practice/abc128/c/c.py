#!/usr/bin/env python3
N, M = map(int,input().split())
KS = [list(map(int, input().split())) for l in range(M)]
P = list(map(int, input().split()))
ans = 0

for n in range(2**N):
    on = 0
    for i in range(M):
        on_switch = 0
        for j in range(1, len(KS[i])):
            if (n>>KS[i][j]-1)&1:
                on_switch += 1
            
        if on_switch % 2 == P[i]:
            on += 1
    
    if on == M:
        ans += 1

print(ans)

# not self AC
