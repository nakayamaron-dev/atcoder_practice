#!/usr/bin/env python3
x = int(input())

def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
 
    return True

fin = False
x -= 1
while fin == False:
    x += 1
    fin = prime_check(x)

print(x)

## AC
