class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        store = [ [0 for i in range (n) ]  for j in range(m) ]
        store[m-1][n-1] = 1
        for i in  range(  m , -1 , -1):
            for j in range ( n , -1 , -1):
                if i < m - 1 and j == n - 1:
                    store[i][j] += store[i + 1][j]
                if j < n - 1  and  i == m -1:
                    store[i][j] += store[i][j+1]
                if j < n - 1 and i < m - 1:
                    store[i][j] +=  store[i + 1][j] + store[i][j+1]
                
                
        # print (store)
        return store[0][0]    
    