#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    num = 1
    ans = 0
    for a in A:
        if a == num:
            num += 1
        else:
            ans += 1
    
    if num == 1:
        return -1
    else:
        return ans

print(main())

# self AC
