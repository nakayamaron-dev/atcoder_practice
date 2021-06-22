#!/usr/bin/env python3
def main():
    X = input()
    M = int(input())
    d = int(max(X))
    l = d
    r = pow(10, 18) + 1

    if len(X) == 1:
        return 1 if d <= M else 0
    
    # 二分探索
    while r - l > 1:
        mid = (l + r) // 2
        s = 0

        #mid進数の計算
        for itm in X:
            s = (s*mid) + int(itm)
        
        if s > M:
            r = mid
        else:
            l = mid
    
    return l - d

print(main())
