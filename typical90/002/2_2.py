#!/usr/bin/env python3
def iter_product(arr, n):
    import itertools
    return list(itertools.product(arr, repeat=n))

def main():
    N = int(input())
    
    for ptn in iter_product([0, 1], N):
        flag1, flag2 = True, False
        cnt = [0, 0]

        # どんなときも "(" が ")" よりも多い
        # "(" と ")"の総数が同じ。
        for n in ptn:
            cnt[n] += 1

            if cnt[0] < cnt[1]:
                flag1 = False
                break
        else:
            if cnt[0] == cnt[1]:
                flag2 = True
        
        if flag1 and flag2:
            print("".join(map(str, ptn)).replace("0", "(").replace("1", ")"))

main()