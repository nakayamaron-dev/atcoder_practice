#!/usr/bin/env python3
import itertools

N, K = map(int, input().split())
T = [input().split() for l in range(N)]
routes = list(itertools.permutations(range(2, N+1)))
times = []

for route in routes:
    route_array = list(route)
    route_array.append(1)
    route_array.insert(0, 1)
    time = 0
    
    for i in range(N):
        time += int(T[route_array[i] - 1][route_array[i+1] - 1])

    times.append(time)

print(times.count(K))

## AC
