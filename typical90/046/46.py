#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        A[i] = A[i] % 46
        B[i] = B[i] % 46
        C[i] = C[i] % 46
    
    cnta = Counter(A)
    cntb = Counter(B)
    cntc = Counter(C)

    for keya, vala in cnta.items():
        for keyb, valb in cntb.items():
            s = (keya+keyb) % 46
            ans += vala * valb * cntc.get((46-s)%46, 0)
    
    return ans

print(main())
