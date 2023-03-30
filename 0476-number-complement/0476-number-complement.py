class Solution:
    def findComplement(self, num: int) -> int:
        y = int.bit_length(num)
        for i in range(y):
            num = (1 << i ^ num)
        return (num)
        