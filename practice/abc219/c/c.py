#!/usr/bin/env python3
def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    def custom_key(word):
        n = []
        for char in word:
            n.append(X.index(char))
        return n

    S.sort(key=custom_key)

    for itm in S:
        print(itm)


main()
