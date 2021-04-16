#!/usr/bin/env python3
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    ans = 0
    for i in range(N):
        ame = sum(A[0][0:i+1]) + sum(A[1][i:])
        ans = max(ame, ans)
        
    return ans

print(main())

# self AC
