class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maximumSpeed = max(piles)
        # minSpeed = min(piles
        left = 1
        right = maximumSpeed
        speed = []
        while left <= right:
            
            mid = ( right + left ) // 2
            total = 0
            for i in range(len(piles)):
                x = piles[i] / mid
                x = ceil(x)
                total += x
           
            if total <= h:
                speed.append(mid)   
                right = mid -1
            else:
                left = mid + 1
                 
                
        return min(speed)            
                    
                
            