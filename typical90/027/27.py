#!/usr/bin/env python3
def main():
    N = int(input())

    cnt = dict()
    for i in range(N):
        S = input()

        if cnt.get(S, "new") == "new":
            cnt[S] = 1
            print(i+1)

main()