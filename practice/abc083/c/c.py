#!/usr/bin/env python3
def main():
    X, Y = map(int,input().split())
    cnt = 0
    while X * 2**(cnt-1) <= Y:
        cnt += 1
    
    return cnt - 1

print(main())

# self AC
