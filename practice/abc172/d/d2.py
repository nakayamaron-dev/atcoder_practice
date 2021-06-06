#!/usr/bin/env python3
def g(n: int):
    return n*(n+1) / 2

def main():
    N = int(input())
    ans = 0

    for i in range(1, N+1):
        ans += i * g(N//i)
    
    return int(ans)

print(main())

# 各倍数の和を足していく方式
# 1の倍数：1+2+...+n
# 2の倍数：2+4+...

# 和の計算方法
# g(n) = n(n+1)/2
# 1の倍数：g(n)
# 2の倍数：2 * g(n//2)
# kの倍数：k * g(n//k)
