class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        x = self.Gcd(a,b)
        return x
    def Gcd(self,a,b):
        if b == 0:
            return a
        return self.Gcd(b , a%b)
        