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

def f(n1, n2):
    return max(len(str(n1)), len(str(n2)))

def main():
    N = int(input())
    divisors = get_divisors(N)
    ans = 10**10+1
    
    for d in divisors:
        ans = min(ans, f(d, N//d))
    
    return ans

print(main())

# self AC
