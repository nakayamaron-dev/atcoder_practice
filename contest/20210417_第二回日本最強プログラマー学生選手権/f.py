N, M, Q = map(int,input().split())

matrix = [[0]*N for _ in range(M)]
ans = 0

for i in range(Q):
    T, X, Y = map(int,input().split())

    if T == 1:
        for i in range(N):
            ans += max(matrix[X-1][i], Y) - matrix[X-1][i]
            matrix[X-1][i] = max(matrix[X-1][i], Y)
    elif T == 2:
        for i in range(M):
            ans += max(matrix[i][X-1], Y) - matrix[i][X-1]
            matrix[i][X-1] = max(matrix[i][X-1], Y)
    
    print(ans)     
