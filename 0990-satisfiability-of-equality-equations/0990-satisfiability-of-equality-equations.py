class Solution:
  
    def equationsPossible(self, equations: List[str]) -> bool:
        s = 0
        for i in equations:
            s = max(s, ord(i[0]) - 97)
            s = max(s, ord(i[3]) - 97)
        
        parent = list(range(s + 1))
        rank = [1] * (s + 1)
        
        def find(x):
            p = parent[x]
            while p != parent[p]:
                p = parent[p]
            parent[x] = p
            return p
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                parent[py] = px
                rank[px] += rank[py]
            
        for i in equations:
            if i[1] == "=":
                union(ord(i[0]) - 97, ord(i[3]) - 97)
        
        for i in equations:
            if i[1] == "!":
                if find(ord(i[0]) - 97) == find(ord(i[3]) - 97):
                    return False
        
        return True