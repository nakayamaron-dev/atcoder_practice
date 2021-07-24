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
    K = int(input())
    ans = 0

    yakusu = get_divisors(K)

    for a in yakusu:
        for b in yakusu:
            c = K / (a*b)
            if c.is_integer() and a <= b <= c:
                ans += 1
    
    return ans

print(main())