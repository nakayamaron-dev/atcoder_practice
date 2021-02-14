# UnionFind
# 素集合を管理するデータ構造
# 素集合を木で持つ
# 木の根を代表とする
# Union:木の根を変で結ぶ
# Find:木の根を報告
from collections import defaultdict

class UnionFind():    
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n+1)

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
         # 根でないなら、親の要素で再検索
        else:
            return self.find(self.par[x])
    
    # x,yがいる集合を併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        return -self.par[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def max_members(self):
        max_members = 0
        for group in self.all_group_members().values():
            if len(group) > max_members:
                max_members = len(group)
            return max_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


