class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        count =  [ i for i in range(1 ,n+1)]
        x = 0
        for i in range(1,len(count)):
            x = (x + k - 1) %  len(count)
            del count[x]
            x = x % len(count)
         
        return (count[0])     
            