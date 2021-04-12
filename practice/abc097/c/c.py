#!/usr/bin/env python3
S = input()
K = int(input())

l = set()
for i in range(1, K+1):
    for j in range(len(S)-i+1):
        l.add(S[j:j+i])

ans = sorted(list(l))
print(ans[K-1])

# not self AC
# 部分点はself AC
# 正解となるのは文字数がK以下になることに気がつけば簡単。
