#!/usr/bin/env python3
def main():
    n, q = map(int,input().split())
    s = input()

    acm = [0]*n
    cnt = 0
    for i in range(1, n):
        if s[i-1:i+1] == "AC":
            cnt += 1
        
        acm[i] = cnt
    
    for _ in range(q):
       l, r = map(int,input().split())
       ans = acm[r-1] - acm[l-1]
       print(ans)

main()

# self AC
