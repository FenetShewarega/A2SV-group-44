class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = {}
        first_occurrence = {}
        last_occurrence = {}

        for i, num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 1
                first_occurrence[num] = i
                last_occurrence[num] = i
            else:
                frequency[num] += 1
                last_occurrence[num] = i

        degree = max(frequency.values())
        min_length = len(nums)

        for num in frequency:
            if frequency[num] == degree:
                length = last_occurrence[num] - first_occurrence[num] + 1
                min_length = min(min_length, length)

        return min_length
        
        
        