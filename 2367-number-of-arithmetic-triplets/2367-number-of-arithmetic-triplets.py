class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

            count = 0
            num_counts = {}

            for num in nums:
                count += num_counts.get(num - diff, 0) * num_counts.get(num - 2 * diff, 0)
                num_counts[num] = num_counts.get(num, 0) + 1

            return count