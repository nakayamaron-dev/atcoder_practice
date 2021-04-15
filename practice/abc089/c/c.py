#!/usr/bin/env python3
def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
    ans = 0
    
    for s in S:
        if dic.get(s[0], "None") != "None":
            dic[s[0]] += 1
    
    dic_fil = dict(filter(lambda x: x[1] > 0, dic.items()))

    if len(dic_fil) == 0: return 0
    
    for p in combinations_array(dic_fil.keys(), 3):
        ans += dic_fil[p[0]] * dic_fil[p[1]] * dic_fil[p[2]]

    return ans

print(main())

# self AC