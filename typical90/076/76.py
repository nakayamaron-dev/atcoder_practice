#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    A += A
    r, cnt = 0, 0

    for l in range(N):
        while cnt*10 < s:
            cnt += A[r]
            r += 1
        
        if cnt* 10 == s:
            return "Yes"
        
        cnt -= A[l]
    else:
        return "No"

print(main())