class Solution:
    def interpret(self, command: str) -> str:
        
        res=""
        n=len(command)
        right=0
        
        while right < n:
        
            if command[right] == "G" :
                res+="G"
                right+=1
                
            elif command[right] == "(":
                
                if command[right + 1] =="a":
                    res+="al"
                    right+=4
                    
                else:
                    res+="o"
                    right+=2
         
                    
        return res            
                
                
                
            
        