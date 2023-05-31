class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        store = [ [0 for i in range (n) ]  for j in range(m) ]
        store[0][0] = 1
        for i in  range(  m ):
            for j in range ( n ):
                if i > 0 and j == 0:
                    store[i][j] += store[i -1 ][j]
                if j > 0  and  i == 0:
                    store[i][j] += store[i][j-1]
                if j > 0 and i > 0:
                    store[i][j] +=  store[i - 1][j] + store[i][j-1]
                
                
        # print (store)
        return store[-1][-1]    
    