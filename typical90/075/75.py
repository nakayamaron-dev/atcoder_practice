#!/usr/bin/env python3
def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list

def main():
    N = int(input())

    x = prime_factorize(N)
    
    if len(x) == 1:
        return 0
    else:
        cnt = 0
        while True:
            if len(x) <= 2**cnt:
                break

            cnt += 1
    
    return cnt

print(main())