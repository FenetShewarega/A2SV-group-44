class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        result = [[0] for _ in range(max(list(counter.values())))]

        for i in range(len(nums)):
            j = 0
            while counter[nums[i]] > 0:
                result[j].append(nums[i])
                j += 1
                counter[nums[i]] -= 1
        
        return [r[1:] for r in result]