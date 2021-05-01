#!/usr/bin/env python3
def main():
    n, m = map(int,input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0

    for bit in range(2**k):
        dish = [0]*n
        cnt = 0
        for i in range(k):
            if (bit>>i) & 1:
                dish[cd[i][1]-1] += 1
            else:
                dish[cd[i][0]-1] += 1
        
        for i in range(m):
            if dish[ab[i][0]-1] != 0 and dish[ab[i][1]-1] != 0:
                cnt += 1
        
        ans = max(ans, cnt)
    
    return ans

print(main())
        
# self AC
