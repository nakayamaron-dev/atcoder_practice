#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    l = []

    for i in range(N):
        a, b = map(int,input().split())
        l.append(b)
        l.append(a-b)
    
    l.sort(reverse=True)
    
    return sum(l[:K])

print(main())
