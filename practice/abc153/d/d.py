#!/usr/bin/env python3
def main():
    h = int(input())
    cnt = 0

    while 2**(cnt+1) <= h:
        cnt += 1
    
    ans = 0
    for i in range(cnt+1):
        ans += 2**i

    return ans

print(main())

# self AC
