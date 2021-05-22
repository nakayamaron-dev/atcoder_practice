#!/usr/bin/env python3
def main():
    N = int(input())
    ans = 0

    for i in range(1, 10**6+1):
        tgt = int(str(i)+str(i))
        if tgt <= N:
            ans += 1
    
    return ans
    
print(main())

# self AC
