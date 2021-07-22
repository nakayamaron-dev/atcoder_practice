#!/usr/bin/env python3
from collections import Counter, deque, defaultdict

def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    dic = defaultdict(int)
    left, ans = 0, 0

    for right in range(N):
        dic[A[right]] += 1

        while len(dic) > K:
            if dic[A[left]] == 1:
                dic.pop(A[left])
            else:
                dic[A[left]] -= 1

            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

print(main())
