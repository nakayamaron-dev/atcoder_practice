#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    KS = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0

    for bit in range(2**N):
        isOk = True
        for m in range(M):
            on = 0
            for itm in KS[m][1:]:
                if (bit >> itm-1) & 1:
                    on += 1
            
            if on % 2 != P[m]:
                isOk = False
        
        if isOk:
            ans += 1
    
    return ans

print(main())

# self AC
