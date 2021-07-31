#!/usr/bin/env python3
from collections import deque
def main():
    N, K = map(int,input().split())
    S = input()

    q = deque()
    ans = ""

    for num, char in enumerate(S):
        while q and q[-1] > char:
            q.pop()
        
        q.append(char)

        if num >= N - K:
            ans += q.popleft()
    
    return ans

print(main())