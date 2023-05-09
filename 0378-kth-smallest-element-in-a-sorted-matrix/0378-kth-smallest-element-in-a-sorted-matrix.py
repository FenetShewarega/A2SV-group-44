class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        store = []
  
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(store,-1 * matrix[i][j])
                if len(store)>k:
                    heappop(store)
        return -1 * store[0]
       