class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        store = [ ]
        heapify(store)
        val = set()
        x = len(matrix)
        for i in range(len(matrix)):
            store.extend(matrix[i])
        store.sort()
        return store[k-1]