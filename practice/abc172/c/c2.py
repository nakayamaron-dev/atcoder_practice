# 方針
# A, Bそれぞれの累積時間で考える。
# Aを固定し、Bを何冊読むか探索する。

#!/usr/bin/env python3
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

cumsum = 0
cumsum_a = [0]
for a in A:
    cumsum += a
    cumsum_a.append(cumsum)  

cumsum = 0
cumsum_b = [0]
for b in B:
    cumsum += b
    cumsum_b.append(cumsum)

r = M
ans = 0
for i in range(N+1):
    if cumsum_a[i] > K:
        break
    # Aを固定した状態で、Bが何冊読めるか
    while cumsum_a[i]+cumsum_b[r] > K:
        r -= 1
    
    ans = max(ans, i+r)

print(ans)

## not self AC
