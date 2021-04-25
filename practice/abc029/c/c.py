#!/usr/bin/env python3
def iter_product(arr, n):
    import itertools
    return list(itertools.product(arr, repeat=n))

def main():
    N = int(input())

    for itm in iter_product("abc", N):
        print("".join(itm))

main()

# self AC
