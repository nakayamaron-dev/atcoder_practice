#!/usr/bin/env python3
import math
def main():
    A, B = map(int, input().split())
    gcd = int(A*B) // int(math.gcd(A,B))
    
    if gcd > 10**18:
        return "Large"
    else:
        return gcd

print(main())