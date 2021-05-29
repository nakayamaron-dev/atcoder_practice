#!/usr/bin/env python3
def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += N / (N-i)
    
    return ans

print(main())

# not self AC
# 解法を知っているかどうかの問題。
