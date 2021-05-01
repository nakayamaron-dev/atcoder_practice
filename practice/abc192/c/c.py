#!/usr/bin/env python3
def g1(n):
    return int("".join(sorted(str(n), reverse=True)))

def g2(n):
    return int("".join(sorted(str(n))))    

def main():
    n, k = map(int,input().split())
    ans = n

    for i in range(1, k+1):
        ans = g1(ans) - g2(ans)
    
    return ans

print(main())
