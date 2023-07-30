class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, curr):
            if len(set(curr)) != len(curr):
                return

            nonlocal max_length
            max_length = max(max_length, len(curr))

            for i in range(start, len(arr)):
                backtrack(i + 1, curr + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length