#!/usr/bin/env python3
N = int(input())
C = [0 if i == "W" else 1 for i in input()]

res = [0]*N
w_to_r = 0
r_to_w = 0
ans = 10**9

for i in range(N):
    # w -> r
    if C[i] == 0 and res[i] == 1:
        w_to_r += 1
    # r -> w
    elif C[i] == 1 and res[i] == 0:
        r_to_w += 1

for i in range(N+1):
    if i == 0:
        cnt = max(r_to_w, w_to_r)
        ans = min(ans, cnt)
    else:
        res[i-1] = 1

        if C[i-1] == res[i-1]:
            r_to_w -= 1
        else:
            w_to_r += 1

        cnt = max(r_to_w, w_to_r)
        ans = min(ans, cnt)
        
print(ans)

## not self AC
