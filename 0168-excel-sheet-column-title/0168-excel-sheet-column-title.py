class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber:
            columnNumber -= 1
            ans += chr((columnNumber) % 26 + ord('A'))
            columnNumber = (columnNumber) // 26

        ans = ans[::-1]
        return ans