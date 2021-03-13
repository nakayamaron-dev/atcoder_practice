#!/usr/bin/env python3
H, W, K = map(int,input().split())
C = []
for i in range(H):
    c = input().replace('.','0').replace('#','1')
    c = [int(i) for i in c]
    C.append(c)
 
 # 範囲が少ないので全探索
ans = 0
for i in range(2**H):
    for j in range(2**W):
        cnt = 0
        for k in range(H):
            for l in range(W):
                if ((i>>k)&1) or ((j>>l)&1):
                    continue
                else:
                    cnt += C[k][l]
        if cnt == K:
            ans += 1
print(ans)

 ## わからない