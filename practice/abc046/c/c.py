#!/usr/bin/env python3
def main():
    N = int(input())
    tk, ao = 1, 1

    for _ in range(N):
        T, A = map(int,input().split())
        k = max((tk+T-1)//T, (ao+A-1)//A)
        tk, ao = k*T, k*A
    
    return tk + ao

print(main())

# not self AC
