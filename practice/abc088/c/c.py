#!/usr/bin/env python3
def main():
    C = [list(map(int, input().split())) for _ in range(3)]
    a = [0,0,0]
    b = [0,0,0]

    for i in range(3):
        b[i] = C[0][i]
        a[i] = C[i][0] - b[0]

    for i in range(3):
        for j in range(3):
            if C[i][j] == a[i] + b[j]:
                continue
            
            return "No"
    
    return "Yes"

print(main())

# not self AC
# a1を0に固定していよいことに気付けるかどうか。
