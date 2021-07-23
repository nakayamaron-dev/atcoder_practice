#!/usr/bin/env python3
def main():
    Q = int(input())
    cards = []

    for _ in range(Q):
        t, x = map(int,input().split())

        if t == 1:
            cards.insert(0, x)
        
        if t == 2:
            cards.append(x)
        
        if t == 3:
            print(cards[x-1])

main()