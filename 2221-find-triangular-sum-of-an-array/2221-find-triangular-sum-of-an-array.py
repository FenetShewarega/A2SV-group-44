class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = nums
        while len(result) > 1:
            newNums = []
            for i in range(len(result) - 1):
                newNums.append((result[i] + result[i+1]) % 10)
            result = newNums
        return result[0]
