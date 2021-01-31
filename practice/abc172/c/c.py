#!/usr/bin/env python3
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=[0]
B=[0]
for i in range(n):
    A.append(A[i]+a[i])
for i in range(m):
    B.append(B[i]+b[i])

ans=0
r=m
for i in range(n+1):
    if A[i]>k:
        break
    while A[i]+B[r]>k:
        r-=1
    ans=max(ans,i+r)
print(ans)

## AC