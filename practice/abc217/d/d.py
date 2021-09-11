from bisect import bisect_left, insort
import array

L, Q = map(int, input().split())
cache = array.array('i', [0, L])

for i in range(Q):
    C, X = map(int, input().split())
    if C == 1:
        idx = insort(cache, X)
    else:
        idx = bisect_left(cache, X)
        print(cache[idx] - cache[idx-1])
