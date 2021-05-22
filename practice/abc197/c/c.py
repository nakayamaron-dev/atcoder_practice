#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = float("inf")

    for bit in range(1 << N-1):
        orx, xor = 0, 0

        for i in range(N):
            # 同じ集合にある値のor演算
            orx |= A[i]

            # 仕切りを入れる場合、xorを更新しorxを初期化。
            if bit >> i & 1:
                xor ^= orx
                orx = 0
        
        xor ^= orx
        ans = min(ans, xor)
    
    return ans

print(main())