class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        tot = 0 
        cnt = 0
        x = tickets[k]
        for i in range(len(tickets)):
            if tickets[i] < x :
                tot += tickets[i]
            else:
                if i > k:
                    cnt+=1
                tot+= x
        return tot-cnt      
                
                
                