N, M = map(int,input().split())
g = [[] for _ in range(N)]
ans = 0
option = [3]*N

for _ in range(M):
    A, B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

if M == 0:
    print(3**N)
    exit()

for i in range(N):
    for j in g[i]:
        option[j] -= 1
        ans += max(option)
    
if max(option) == 0:
    print(0)
else:
    print(ans)

