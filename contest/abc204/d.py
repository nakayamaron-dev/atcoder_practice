def main():
    N = int(input())
    T = list(map(int, input().split()))
    s = sum(T)

    dp = [[0]*(s+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1
    
    for i in range(1, N+1):
        for j in range(s):
            if dp[i-1][j] == 1:
                dp[i][j+T[i-1]] = 1
                dp[i][j] = 1
    
    mi = float("inf")
    for j in range(s+1):
        if dp[-1][j]:
            ma = max(j, s-j)
            mi = min(mi, ma)
    
    return mi

print(main())