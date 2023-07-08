class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def gp(nums, permutation, bit, permutations):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if not (bit & (1 << i)):
                    permutation.append(nums[i])
                    bit |= (1 << i)
                    gp(nums, permutation, bit, permutations)
                    bit &= ~(1 << i)
                    permutation.pop()
        
        permutations = []
        gp(nums, [], 0, permutations)
        return permutations