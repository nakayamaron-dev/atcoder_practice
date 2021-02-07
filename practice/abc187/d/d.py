#!/usr/bin/env python3
N = int(input())
X = 0
x = []
for i in range(N):
    A, B = map(int, input().split())
    X -= A
    x.append(A + A + B)
x.sort()
ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print(ans)

# X = 高橋の票数 - 青木の票数
# 高橋がある街で演説すると、Xは2Ai + Bi票増える。
# X > 0 になれば終わり
