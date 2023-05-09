class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] *= -1
        heapify(piles)
        for i in range(k):
           
            x = heappop(piles)
            x = x // 2
            heappush(piles , x)
        return(sum(piles) * - 1 )
