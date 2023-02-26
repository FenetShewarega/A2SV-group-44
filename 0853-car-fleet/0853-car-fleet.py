class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack  = []
        c = defaultdict(int)
        count = 0  
       
        for i in range(n):
            c[position[i]] += speed[i]
        
        c = sorted(c.items()  , key = lambda x:x[0] , reverse = True)
              
        for i , j in c:
            val = (target - i) / j
            stack.append(val)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            
        return(len(stack))       
                
                    
                    

                    
                    