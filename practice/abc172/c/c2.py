#!/usr/bin/env python3
def main():
    n, m, k = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A, B = [0], [0]

    for i in range(n):
        A.append(A[i]+a[i])
    for i in range(m):
        B.append(B[i]+b[i])

    ans = 0
    for i in range(n+1):
        if A[i] > k:
            break 
        while A[i] + B[m] > k:
            m -= 1
        ans = max(ans, i+m)
    
    return ans

print(main())
        
# not self AC
# 累積時間、　Aを固定してBの読める本数を考える
# もう一度挑戦する。
