class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = {}
        max_length = 1

        for num in arr:
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])

        return max_length               