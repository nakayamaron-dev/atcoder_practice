#!/usr/bin/env python3
def main():
    h, w, k = map(int,input().split())
    c = []
    ans = 0

    black = 0
    for i in range(h):
        row = list(map(str, input().split()))
        c.append(row[0])
        black += c[i].count("#")
    
    for h_bit in range(2**h):
        for w_bit in range(2**w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if (h_bit>>i)&1 or (w_bit>>j)&1:
                        if c[i][j] == "#":
                            cnt += 1
            
            if black - cnt == k:
                ans += 1
    
    return ans

print(main())

# self AC
