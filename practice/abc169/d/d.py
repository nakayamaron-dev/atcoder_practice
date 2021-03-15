#!/usr/bin/env python3
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
factor = factorization(N)
ans = 0

if N == 1:
    print(0)
else:
    for f in factor:
        loop = True
        cnt = 1
        while loop:
            f[1] -= cnt
            cnt += 1
            ans += 1

            if f[1] - cnt < 0:
                loop = False

    print(ans)

## self AC
# 素因数分解ができれば簡単
