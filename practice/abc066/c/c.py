#!/usr/bin/env python3
from collections import deque
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = deque()

    for i in range(N):
        if i%2 == 1:
            ans.appendleft(A[i])
        else:
            ans.append(A[i])
    
    if N % 2 == 0:
        return ans
    else:
        ans.reverse()
        return ans

print(*main())

# not self AC
