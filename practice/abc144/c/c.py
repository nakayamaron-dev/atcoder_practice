#!/usr/bin/env python3
n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisors = make_divisors(n)
ptn= 0
ans = n

if len(divisors) % 2 == 0:
    ptn = len(divisors) // 2
else:
    ptn = len(divisors) // 2 + 1

for i in range(1, ptn+1):
    i_x = divisors[i]
    i_y = n // i_x
    dist = i_x + i_y - 2

    if dist < ans:
        ans = dist

print(ans)

## AC
