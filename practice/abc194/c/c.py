#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    ans = 0

    for i in range(-200, 200):
        for j in range(i+1, 201):
            ans += c[i]*c[j]*(abs(i-j)**2)
    
    return ans

print(main())

# not self AC
# Ai - Ajの組み合わせが200*200=40000通りなので、全探索する。
