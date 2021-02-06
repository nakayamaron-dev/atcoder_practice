#!/usr/bin/env python3
n = int(input())
b = list(map(int, input().split()))

a = [0]*(n)

for i in range(len(a)):
  if (i == 0):
    a[i] = b[i]
  elif i == len(a)-1:
    a[i] = b[i-1]
  else:
    a[i] = min(b[i-1], b[i])
    
print(sum(a))

## AC
