#!/usr/bin/env python3
def main():
    n = int(input())
    maxval = int(n**0.5) + 1
    ans = set()
    
    for a in range(2, maxval):
        for b in range(2, n+1):
            if a**b > n:
                break
            else:
                ans.add(a**b)
    
    return n - len(ans)

print(main())

# self AC
