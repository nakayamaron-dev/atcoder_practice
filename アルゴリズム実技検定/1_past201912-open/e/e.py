#!/usr/bin/env python3
def main():
    n, q = map(int,input().split())

    # 隣接リストの初期化
    g = [[False]*n for _ in range(n)]

    for i in range(q):
        query = list(map(int, input().split()))
        a = query[1]-1

        if query[0] == 1:
            b = query[2]-1
            g[a][b] = True
        elif query[0] == 2:
            for v in range(n):
                if g[v][a]:
                    g[a][v] = True
        else:
            # リアルタイムで更新してしまうとだめなので、一時的にリストに格納しておき、最後にまとめて更新する。
            to_follow = []

            for v in range(n):
                if g[a][v]:
                    for w in range(n):
                        if g[v][w] and w != a:
                            to_follow.append(w)
            
            for w in to_follow:
                g[a][w] = True
        
    for i in range(n):
        for j in range(n):
            if g[i][j]:
                print("Y", end="")
            else:
                print("N", end="")  
        print()

main()

# not self AC
