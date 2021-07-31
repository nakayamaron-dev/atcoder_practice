#!/usr/bin/env python3
# 無向辺バージョン
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
 
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
    H, W = map(int,input().split())
    Q = int(input())
    uf = UnionFind(H*W)
    mas = [[0]*W for _ in range(H)]

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            h, w = q[1]-1, q[2]-1
            mas[h][w] = 1

            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nh, nw = h+y, w+x
                
                if not (0 <= nh < H and 0 <= nw < W):
                    continue

                if mas[nh][nw] == 1:
                    uf.union(nh*W + nw, h*W + w)
        else:
            h1, w1 = q[1]-1, q[2]-1
            h2, w2 = q[3]-1, q[4]-1

            if mas[h1][w1] == 0 and mas[h2][w2] == 0:
                print("No")
                continue

            i1, i2 = h1*W + w1, h2*W + w2

            if uf.same(i1, i2):
                print("Yes")
            else:
                print("No")

main()