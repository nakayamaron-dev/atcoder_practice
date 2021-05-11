from collections import deque
 
n = int(input())

g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, i))
    g[b].append((a, i))
 
edge = [0] * (n - 1)
parent = [-1] * n
 
q = deque()
q.append(0)
num_color = 0

# dfs
while len(q):
    now = q.popleft()
    color = 1
    ng_color = parent[now]
    for v, e in g[now]:
        #未訪問かどうか
        if edge[e] == 0:
            if color == ng_color:
                color+=1
            num_color = max(num_color, color)
            edge[e] = color
            parent[v] = color
            color+=1
            q.append(v)

print(num_color)
print(*edge, sep='\n')

# not self AC
# dfsの復習が必要。
