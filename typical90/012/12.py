#!/usr/bin/env python3
from collections import deque
from collections import defaultdict
# 無向辺バージョン
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
    mas = [[0]*W for _ in range(H)]
    uf = UnionFind(H*W)

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            h, w = q[1]-1, q[2]-1
            mas[h][w] = 1

            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                h_ = h + y
                w_ = w + x

                # マス領域外の場合スキップ
                if not (0 <= h_ < H and 0 <= w_ < W):
                    continue

                # 上下左右が赤色であれば、UnionFindで結合する。
                if mas[h_][w_] == 1:
                    # マスをflatにした場合の順番で結合する。
                    uf.union(h_*W + w_, h*W + w)
        else:
            h1, w1 = q[1]-1, q[2]-1
            h2, w2 = q[3]-1, q[4]-1

            if mas[h1][w1] == 0 or mas[h2][w2] == 0:
                print("No")
                continue

            i1, i2 = h1*W + w1, h2*W + w2

            if uf.same(i1, i2):
                print("Yes")
            else:
                print("No")

main()
