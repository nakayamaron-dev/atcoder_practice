#!/usr/bin/env python3
def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))


S1 = list(input())
S2 = list(input())
S3 = list(input())
s = list(set(S1+S2+S3))

# 11種類より多い場合、あり得ないので終了
if len(s) > 10 or (len(S3)-len(S1) >= 2 and len(S3)-len(S2) >= 2) or len(S3) < len(S1) or len(S3) < len(S2):
    print('UNSOLVABLE')
    exit()

for ptn in permutations_array(range(0, 10), len(s)):
    dic = dict()
    for i in range(len(s)):
        dic[s[i]] = ptn[i]

    if dic[S1[0]] == 0 or dic[S2[0]] == 0 or dic[S3[0]] == 0:
        continue

    n1 = int("".join([str(dic[x]) for x in S1]))
    n2 = int("".join([str(dic[x]) for x in S2]))
    n3 = int("".join([str(dic[x]) for x in S3]))

    if n1 + n2 == n3:
        print(n1)
        print(n2)
        print(n3)
        break
else:
    print('UNSOLVABLE')
