#!/usr/bin/env python3
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))
    shift = 0

    for _ in range(Q):
        t, x, y =  map(int,input().split())
        x, y = x-1, y-1

        if t == 1:
            x, y = (x - shift) % N, (y - shift) % N
            A[x], A[y] = A[y], A[x]
        elif t == 2:
            shift += 1
        else:
            x = (x - shift) % N
            print(A[x])

main()
