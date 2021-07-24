#!/usr/bin/env python3
from itertools import product
def main():
    N = int(input())
    ans = []

    if N % 2 == 0:
        for ptn in product((1, 0), repeat=N):
            cnt = [0, 0]
            flag1 = False
            flag2 = True

            flag1 = (sum(ptn) ==  N//2)

            for j in ptn:
                cnt[j] += 1
                # どんなときも"("が")"より少なくなることはない。
                if cnt[0] < cnt[1]:
                    flag2 = False
                    break
            
            if flag1 and flag2:
                ans.append("".join(map(str, ptn)).replace("0", "(").replace("1", ")"))
            
        print("\n".join(sorted(ans)))

main()
