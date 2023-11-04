class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        

        b = {index: number for index, number in enumerate(nums)}
        num = sorted(nums)
        a = {index: number for index, number in enumerate(num)}

        left = 0 
        right = len(nums) - 1
        
        while  left < len(num) and right > 0:
            
            if num[left] + num[right] > target:
                right -= 1
            elif num[left] + num[right] < target:
                left += 1
            else:
                break
        print(left , right)
        sol = []
        left = a[left]
        right = a[right]
        print(left , right)
        for key , val in b.items():
            if val == left or val == right:
                sol.append(key)
        return sol
            
                