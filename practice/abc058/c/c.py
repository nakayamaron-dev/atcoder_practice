#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    common = dict()

    for i in range(N):
        if i == 0:
            common = Counter(S[i])
            continue

        for key, val in common.items():
            if Counter(S[i]).get(key, "None") != "None":
                common[key] = min(val, Counter(S[i])[key])
            else:
                common[key] = 0

    ans = ""
    common = sorted(common.items(), key=lambda x:x[0])
    for key, val in common:
        ans += key * val
    
    return ans

print(main())

# self AC
