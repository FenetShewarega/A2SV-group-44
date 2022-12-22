class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        res = -1
        cal = math.inf
        for i in range(len(points)):
            
            if x == points[i][0] or y == points[i][1]: 
                ans = abs(x - points[i][0]) + abs(y-points[i][1])
                
                if ans < cal:
                    res = i
                    cal = ans
                
        return res
                 
                