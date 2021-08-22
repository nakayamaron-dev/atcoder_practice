#!/usr/bin/env python3
def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))


def main():
    S, K = input().split()
    K = int(K)
    S = list(S)

    ptn = permutations_array(S, len(S))
    ptn = sorted(list(set(ptn)))

    return "".join(ptn[K-1])


print(main())
