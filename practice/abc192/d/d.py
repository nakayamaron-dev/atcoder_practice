#!/usr/bin/env python3
def main():
    X = input()
    M = int(input())
    d = int(max(X))
    l = len(X)

    if l == 1:
        if d <= M: return 1
        else: return 0
    
    p = d
    k = pow(10, 18) + 1

    # 二分探索
    while (k - p) > 1:
        r = (k + p) // 2
        s = 0
        for n in X:
            s = (s*r) + int(n)
        
        if s > M:
            k = r
        else:
            p = r
    
    return p - d

print(main())

# not self AC
# 二分探索
