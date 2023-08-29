class Solution:
    def maxProfit(self, prices: List[int]) -> int:
   
        profit1 = 0
        profit2 = 0
        
        for p in range( 1 , len(prices)):
            hold = profit1
            
            profit1 =max(profit1+prices[p]-prices[p-1], profit2)
            profit2 =  max(hold, profit2)
        return max(profit1 , profit2)
