def main():
    N, K = map(int,input().split())
    ans = 0

    for n in range(1,N+1):
        for k in range(1, K+1):
            room = n * 100 + k
            ans += room
    
    return ans

print(main())