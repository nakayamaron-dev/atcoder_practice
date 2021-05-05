#!/usr/bin/env python3
def main():
    A, R, N = map(int,input().split())

    if R == 1:
        return A
    
    for i in range(N-1):
        A *= R

        if A > 10**9:
            return "large"
    
    return A

print(main())

# self AC
