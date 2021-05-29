#!/usr/bin/env python3

# 低くできる場合は低くする。
def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N):
        if i == 0:
            H[i] -= 1
        else:
            if H[i] > H[i-1]:
                H[i] -= 1
            
            # 非単調減少かどうか判定
            if H[i] < H[i-1]:
                return "No"
    
    return "Yes"

print(main())

# self AC
