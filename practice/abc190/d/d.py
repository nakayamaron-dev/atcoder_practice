#!/usr/bin/env python3
def get_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    N = int(input())
    div = get_divisors(N)
    ans = 0

    for itm in div:
        if itm % 2 != 0:
            ans += 2
    
    return ans

print(main())

# self AC
# 奇数の約数の数の2倍あることに気づけたら簡単。
