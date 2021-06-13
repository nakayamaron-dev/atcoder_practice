#!/usr/bin/env python3
def main():
    S = input()

    # dp
    A = [0] * 2019
    A[0] = 1

    ans, x, p = 0, 0, 1
    for char in S[::-1]:
        x = (x + int(char) * p) % 2019
        p = (p * 10) % 2019
        ans += A[x]
        A[x] += 1
    
    return ans

print(main())

# 2019と10が互いに素であることを利用し、X * 10^nが2019の倍数であれば、X * 10^(n-1)も2019の倍数となる。
# 上記を利用すると、累積和の考え方とDPで高速に解ける。
# 