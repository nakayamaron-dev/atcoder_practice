#!/usr/bin/env python3
N, K = map(int,input().split())
A = [0] + [int(i) for i in input().split()]

i=1
cnt=0
visited=[]
visited.append(1)
v=set([1])
while (A[i] not in v) and cnt<K:
    visited.append(A[i])
    v.add(A[i])
    i=A[i]
    cnt+=1
    
if A[i] in visited:
    x=visited.index(A[i])
    y=len(visited)
    print(visited[(K-x)%(y-x)+x])
else:
    print(visited[-1])

## not self AC
