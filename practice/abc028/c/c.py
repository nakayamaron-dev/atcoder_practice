#!/usr/bin/env python3
def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

def main():
    A, B, C, D, E = map(int,input().split())
    ans = set()

    for itm in combinations_array([A,B,C,D,E], 3):
        ans.add(sum(list(itm)))
    
    ans = list(ans)
    ans.sort(reverse=True)
    return ans[2]

print(main())

# self AC
