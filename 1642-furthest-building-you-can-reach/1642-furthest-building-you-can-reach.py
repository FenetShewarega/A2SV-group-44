class Solution:
    def furthestBuilding(self,heights, bricks, ladders):
        diffs = [] 
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(diffs, diff) 
                if len(diffs) > ladders:
                    bricks -= heapq.heappop(diffs) 
                if bricks < 0:
                    return i - 1  
        return len(heights) - 1 
