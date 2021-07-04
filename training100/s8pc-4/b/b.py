#!/usr/bin/env python3
def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    ans = 10 ** 18
    
    for case in combinations_array(range(1, N), K-1):
        cost = 0
        base = A[0]
        for i in range(1, N):
            if i in case:
                base = max(base+1, A[i])
                cost += base - A[i]
            else:
                base = max(base, A[i]) 
        
        ans = min(ans, cost)
    
    return ans

print(main())