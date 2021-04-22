#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    D = list(map(str, input().split()))
    money = N

    while True:
        dup = set(str(money)) & set(D)

        if len(dup) == 0:
            return money
        
        money += 1

print(main())

# self AC
