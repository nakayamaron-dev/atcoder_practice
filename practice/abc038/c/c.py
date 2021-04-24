#!/usr/bin/env python3
def calc_factorial_sum(n):
    ans = 0
    for i in range(1, n):
        ans += i
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = len(A)
    start = 0
    end = 0

    for i in range(N-1):
        if A[i+1] <= A[i]:
            ans += calc_factorial_sum(end-start+1)
            start = i+1
            end = i+1
        else:
            end += 1
            if i == N-2:
                ans += calc_factorial_sum(end-start+1)
                
    return ans

print(main())

# self AC
