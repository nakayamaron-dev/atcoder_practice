#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    A.extend(A)
    choice, r = 0, 0

    for l in range(N):
        while choice*10 < s:
            choice += A[r]
            r += 1
        
        if choice*10 == s:
            return "Yes"
        else:
            choice -= A[l]
    else:
        return "No"

print(main())