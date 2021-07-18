#!/usr/bin/env python3
def main():
    N = int(input())
    MAX = 10**6 + 2
    table = [0] * MAX

    # いもす法の典型パターン
    for _ in range(N):
        a, b = map(int,input().split())
        table[a] += 1
        table[b+1] -= 1

    for i in range(1, MAX):
        table[i] += table[i-1]
    
    return max(table)

print(main())