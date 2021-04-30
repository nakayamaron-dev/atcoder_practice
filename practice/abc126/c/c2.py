#!/usr/bin/env python3
def main():
    n, k = map(int,input().split())
    ans = 0
    r = 1 / n

    for i in range(1, n+1):
        score = i
        cnt = 0
        while score < k:
            score *= 2
            cnt += 1
        
        ans += r * (0.5)**(cnt)
    
    return ans

print(main())

# self AC
