class Solution:
    def countBinarySubstrings(self, s):
        ans = 0
        left = 0
        right  = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(left, right)
                left, right = right, 1
            else:
                right += 1

        return ans + min(left, right)