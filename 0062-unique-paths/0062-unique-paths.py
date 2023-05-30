class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        self.store = defaultdict(tuple)
        return self.pathtracker(0 , 0 , m - 1, n - 1)
    
    def pathtracker(self,i , j , m , n):
        
        if i == m and j == n:
            return 1
        if (i , j) not in self.store:
            
            if i == m and j < n :
                self.store[(i , j)] = self.pathtracker(i  , j + 1 , m, n )
            if j == n and i < m:
                self.store[(i , j)] = self.pathtracker(i  + 1, j , m, n )
            if j < n and i < m:
                self.store[(i , j)] = self.pathtracker(i+1 ,j , m , n) + self.pathtracker(i , j + 1, m ,n)

        return self.store[(i , j)]