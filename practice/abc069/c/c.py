#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    mul2, mul4, other = 0, 0, 0
    for a in A:
        if a % 4 == 0:
            mul4 += 1
        elif a % 2 == 0:
            mul2 += 1
        else:
            other += 1
    
    if mul2 % 2 == 1:
        other += 1
    
    if other - 1 > mul4:
        return "No"
    else:
        return "Yes"

print(main())

# self AC
