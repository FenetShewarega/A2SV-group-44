class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = int.bit_length(n)
        stack=[]
        count = 0
        for i in range(length):
            if (1 << i) & n:
                if stack and stack[-1] == "x":
                    return False
                stack.append("x")
            else:
                if stack and stack[-1] == "y":
                    return False
                stack.append("y")
        print(stack)
        return True
        