class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        N = len(nums)

        def helper(left , right ):
            
            if  left > right :
                return 0
        
            choiceLeft = nums[left] - helper(left + 1 ,  right)
            choiceRight = nums[right] - helper(left , right - 1)
            
            return (max(choiceLeft , choiceRight))

        return helper( 0, N - 1) >= 0

            
        