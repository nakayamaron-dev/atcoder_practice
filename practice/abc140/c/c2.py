#!/usr/bin/env python3
N = int(input())
B = list(map(int, input().split()))

ans = []
if len(B) != 1:
    for i in range(len(B)):
        if i == 0:
            ans.append(B[0])
        elif i == len(B)-1:
            ans.append(min(B[i-1], B[i]))
            ans.append(B[i])
        else:
            ans.append(min(B[i-1], B[i]))
else:
    ans.append(B[0])
    ans.append(B[0])

print(sum(ans))

## self AC
