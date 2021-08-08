from collections import deque
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    g = [[]*N for _ in range(N)]

    for _ in range(N-1):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    #ソート
    for idx, itm in enumerate(g):
        g[idx] = sorted(itm)
    
    visited = [False] * N
    visited[0] = True
    ans = deque()
    ans.append(1)

    def dfs(pre, cur):
        no_move = True
        for i in g[cur]:
            if visited[i]:
                continue

            ans.append(i+1)
            visited[i] = True
            no_move = False
            dfs(cur, i)
        
        if no_move:
            if cur == 0:
                return
            else:
                ans.append(pre+1)
                dfs(cur, pre)
    
    dfs(-1,0)
    return ans

print(*main())

# オイラーツアーというらしい。