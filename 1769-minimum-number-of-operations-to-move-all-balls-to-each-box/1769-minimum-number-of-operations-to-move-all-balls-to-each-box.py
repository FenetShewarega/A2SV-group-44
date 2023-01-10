class Solution:
 
    def minOperations(self, boxes: str) -> List[int]:
        
        left = 0 
        out_put = []
        # count  = 0
        # boxes = list(boxes)
        for i in range (len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if boxes[j] ==  "1":
                    count +=  abs(i-j)
                # tot = count         
            out_put.append(count)
           
            
        return out_put
            
            
            
            
          
                        
                    
                    


            
        
        