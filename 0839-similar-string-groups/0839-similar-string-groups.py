class Solution:
    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.parent = {i: i for i in range(len(strs))}
        self.rank = {i: 1 for i in range(len(strs))}

        def union(x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                word1, word2 = strs[i], strs[j]
                if self.areSimilar(word1, word2):
                    union(i, j)

        groups = set()
        for i in range(len(strs)):
            groups.add(self.find(i))

        return len(groups)

    def areSimilar(self, word1, word2):
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                count += 1
                if count > 2:
                    return False
        return True