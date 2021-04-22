#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    arr = []

    for i in range(N):
        arr.append([A[i], i+1])
    
    arr.sort(reverse=True)

    for a in arr:
        print(a[1])

main()

# self AC
