class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
      
        
        for i in range(len(stones)):
            stones[i] = (stones[i]) * -1
    
        heapify(stones)
        while len(stones) > 1:
            x= -1*(heappop(stones))
            y= -1*(heappop(stones))
            if x > y:
                heappush(stones ,-1*(x - y))
        if stones:
            return(-1*(stones[0]))
        else:
            return 0