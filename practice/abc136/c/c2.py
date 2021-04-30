#!/usr/bin/env python3
def main():
    n = int(input())
    h = list(map(int, input().split()))

    for i in range(n-1):
        if h[i+1]-1 >= h[i]:
            h[i+1] -= 1
        elif h[i+1] >= h[i]:
            continue
        else:
            return "No"
    
    return "Yes"

print(main())

# not self AC
# 1引いても単調非減少であれば後の選択肢を増やすために1引く
