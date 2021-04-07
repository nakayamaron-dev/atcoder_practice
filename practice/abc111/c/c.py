#!/usr/bin/env python3
def counter_most_common(arr):
    from collections import Counter
    return Counter(arr).most_common()

N = int(input())
V = list(map(int, input().split()))

ctr_0 = counter_most_common(V[::2])
ctr_1 = counter_most_common(V[1::2])

# 最も多い要素が異なっている場合、それ以外の要素を全て変更する必要がある。
if ctr_0[0][0] != ctr_1[0][0]:
    print(N - ctr_0[0][1] - ctr_1[0][1])
else:
    # 最も多い要素が同じ、かつ要素数が1つしかない場合、全て同じ値なので半分の要素を全て変更する必要がある。
    if len(ctr_0) == len(ctr_1) == 1:
        print(N//2)
    # 最も多い要素が同じ場合、2番目に多い要素が大きい方をtakeする。
    else:
        a = N-ctr_0[0][1]-ctr_1[1][1]
        b = N-ctr_0[1][1]-ctr_1[0][1]
        print(min(a,b))

# not self AC    
