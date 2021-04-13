#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    A.append(0)

    dist_all = 0
    # 最初に累積距離を求めておく。
    for i in range(1, N+2):
        dist_all += abs(A[i] - A[i-1])
    
    for i in range(1, N+1):
        dist = dist_all - abs(A[i]-A[i-1]) - abs(A[i]-A[i+1]) + abs(A[i-1]-A[i+1])
        print(dist)

main()

# self AC

