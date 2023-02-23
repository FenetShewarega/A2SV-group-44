class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        total = 0
        self.prefix = [] 
        for i in range(len(self.nums)):
           
            self.prefix.append(total)
            total+= self.nums[i]
        self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        return ( self.prefix[right + 1] - self.prefix[left ])
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)