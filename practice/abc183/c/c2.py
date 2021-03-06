#!/usr/bin/env python3
N, K = map(int,input().split())
l = [list(map(int, input().split())) for l in range(N)]

def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

cities = [x for x in range(1, N+1)]
routes = permutations_array(cities[1:], len(cities[1:]))
dists = []

for route in routes:
    route = list(route)
    route.insert(0, 1)
    route.append(1)
    dist = 0
    
    for idx in range(1, N+1):
        dist += l[route[idx-1]-1][route[idx]-1]

    dists.append(dist)

ans = dists.count(K)
print(ans)

# self AC
