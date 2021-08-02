#!/usr/bin/env python3
from collections import defaultdict
def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    dic = defaultdict(int)
    l, ans = 0, 0

    for r in range(N):
        dic[A[r]] += 1

        # K種類以下になるまでwhile。
        # 左側から見ていき、1つしかない場合はpop, 2つ以上ある場合は-1する。
        while len(dic) > K:
            if dic[A[l]] == 1:
                dic.pop(A[l])
            else:
                dic[A[l]] -= 1
            
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

print(main())