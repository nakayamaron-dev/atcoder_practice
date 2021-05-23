import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())
    ans = [0]*N

    g = [[] for _ in range(N)]
    for idx, parent in enumerate(P):
        g[parent-1].append(idx+1)
    
    for i in range(Q):
        U, D = map(int,input().split())
        U -= 1
        D -= 1

        def dfs(cur, visited: list):
            for p in g[cur]:
                visited.append(p)

                if U in visited and cur == D:
                    ans[i] += 1
                    visited.pop(-1)
                else:
                    dfs(p, visited)
        
        dfs(0, [0])
        print(ans[i])

main()
