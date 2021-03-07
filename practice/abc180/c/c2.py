# Nの約数を列挙できれば終了。

#!/usr/bin/env python3
N = int(input())

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

divisors = get_divisors(N)

for divisor in divisors:
    print(divisor)

## self AC