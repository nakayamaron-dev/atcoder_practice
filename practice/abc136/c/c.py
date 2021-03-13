#!/usr/bin/env python3
N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):
    # 1引いても単調非減少であれば後の選択肢を増やすために1引く
    if H[i+1]-1 >= H[i]:
        H[i+1] -= 1
    elif H[i+1] >= H[i]:
        continue
    else:
        print("No")
        exit()

print("Yes")

## not self AC
