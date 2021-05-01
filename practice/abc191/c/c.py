#!/usr/bin/env python3
def main():
    h, w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0

    for i in range(h-1):
        for j in range(w-1):
            f1 = s[i][j]
            f2 = s[i][j+1]
            f3 = s[i+1][j]
            f4 = s[i+1][j+1]
            tgt = [f1, f2, f3, f4]

            if tgt.count("#") % 2 == 1:
                ans += 1
        
    return ans

print(main())

# self AC
# 気付けるかどうか。
