#!/usr/bin/env python3
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))
    shift = 0

    for _ in range(Q):
        T, X, Y = map(int,input().split())
        X, Y = X-1, Y-1

        if T == 1:
            X, Y = (X-shift) % N, (Y-shift) % N
            A[X], A[Y] = A[Y], A[X]

        if T == 2:
            shift += 1
        
        if T == 3:
            idx = (X - shift) % N
            print(A[idx])

main()