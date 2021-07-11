def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    C.sort()

    for i in range(N):
        ans *= (C[i] - i)
        ans %= mod
    
    return ans


print(main())