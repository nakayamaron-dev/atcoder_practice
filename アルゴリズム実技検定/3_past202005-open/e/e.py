#!/usr/bin/env python3
def main():
    n, m, q = map(int,input().split())
    g = [[] for _ in range(n)]

    for i in range(m):
        u, v = map(int,input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    
    c = list(map(int, input().split()))

    for i in range(q):
        query = list(map(int, input().split()))
        x = query[1]
        x -= 1

        print(c[x])

        if query[0] == 1:
            for i in g[x]:
                c[i] = c[x]
        
        if query[0] == 2:
            y = query[2]
            c[x] = y    

main()

# not self AC
