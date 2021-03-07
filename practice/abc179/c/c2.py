#!/usr/bin/env python3

# 方針
# N未満のAxBの組み合わせを探索し、余りはCで補える。
# C >= 1より、N未満のAxBの組み合わせを探索する。

N = int(input())

ans = 0
for a in range(1, N): # 1 ~ N-1
    ans += (N-1) // a

print(ans)

## self AC
