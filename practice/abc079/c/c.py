#!/usr/bin/env python3
def iter_product(arr, n):
    import itertools
    return list(itertools.product(arr, repeat=n))

def main():
    N = input()
    ptn = iter_product(["+", "-"], 3)

    for p in ptn:
        ans = int(N[0])
        for i in range(3):
            if p[i] == "+":
                ans += int(N[i+1])
            else:
                ans -= int(N[i+1])
        
        if ans == 7:
            return "{}{}{}{}{}{}{}=7".format(N[0], p[0], N[1], p[1], N[2], p[2], N[3])

print(main())

# self AC
