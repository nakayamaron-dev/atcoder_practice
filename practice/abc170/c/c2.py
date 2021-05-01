#!/usr/bin/env python3
def main():
    x, n = map(int,input().split())
    p = list(map(int, input().split()))

    if x not in p:
        return x
    
    cnt = 0
    while True:
        cnt += 1
        if x - cnt not in p:
            return x - cnt
        
        if x + cnt not in p:
            return x + cnt
    
print(main())

# self AC
