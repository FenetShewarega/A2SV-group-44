class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generateParentheses(current, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(current)
                return

            if open_count < n:
                generateParentheses(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                generateParentheses(current + ")", open_count, close_count + 1)

        generateParentheses("", 0, 0)
        return result