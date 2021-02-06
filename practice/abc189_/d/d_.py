#!/usr/bin/env python3
n = int(input())
s = [str(input()) for _ in range(n)]

ans = 1
for i in range(n):
    if s[i] == 'AND': # 最後の項は必ずTrueである必要があるので、個数は同じ
        continue
    else: # ORの場合、最後の項がTrueであれば以前は何でもよい、Falseであればn-1の解がTrueである必要がある。
        ans = ans + 2**(i+1)

print(ans)

## AC
