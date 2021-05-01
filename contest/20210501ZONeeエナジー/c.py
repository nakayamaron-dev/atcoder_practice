N = int(input())
ABCDE = [list(map(int, input().split())) for _ in range(N)]
ans = -float("inf")

# TLE
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            p = max(ABCDE[i][0],ABCDE[j][0],ABCDE[k][0])
            s = max(ABCDE[i][1],ABCDE[j][1],ABCDE[k][1])
            t = max(ABCDE[i][2],ABCDE[j][2],ABCDE[k][2])
            k = max(ABCDE[i][3],ABCDE[j][3],ABCDE[k][3])
            i = max(ABCDE[i][4],ABCDE[j][4],ABCDE[k][4])

            total = min(p,s,t,k,i)
            ans = max(ans, total)

print(ans)

# 
