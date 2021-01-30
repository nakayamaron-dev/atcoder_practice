N = int(input())
ans = 0

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

divisors = make_divisors(N)

for divisor in divisors:
    if divisor % 2 == 1:
        ans += 2

print(ans)

## AC
