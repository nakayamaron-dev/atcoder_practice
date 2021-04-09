#!/usr/bin/env python3
N, K = map(int,input().split())

ans = (N//K)**3
if K % 2 == 1:
    print(ans)
else:
    mod = K // 2
    cnt = 0
    while mod <= N:
        cnt +=1
        mod += K
    
    ans += cnt**3
    print(ans)

# self AC
    