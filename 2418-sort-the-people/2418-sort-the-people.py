class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            min_val = i
            for j in range(i,len(names)):
                
                
                 if heights[min_val] <  heights[j]:
                        min_val = j
            heights[i] , heights[min_val] =  heights[min_val] , heights[i]
            names[i] ,  names[min_val] =  names[min_val] , names[i]
        return names   
            
                        
            
                    
        
        