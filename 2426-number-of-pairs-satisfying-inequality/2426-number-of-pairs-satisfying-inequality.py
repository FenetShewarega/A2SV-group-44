class Solution:
    def merge(self, low, mid, high, nums, diff):
        count = 0
        l, r = low, mid+1
        while l <= mid and r <= high:
            
            if nums[l] <= nums[r] + diff:
                
                
                
                count += high - r + 1
                l += 1
            else:
                r += 1
                
                
#         r+= 1
#         l += 1
                
                
                
                
        nums[low:high+1] = sorted(nums[low:high+1])
        return count

    def mergeSort(self, low, high, nums, diff):
        if low >= high:
            return 0
        
        
        
        
        
        pairs = 0
        mid = (low+high) // 2
        pairs += self.mergeSort(low, mid, nums, diff)
        pairs += self.mergeSort(mid+1, high, nums, diff)
        pairs += self.merge(low, mid, high, nums, diff)
        return pairs

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(n)]
        return self.mergeSort(0, n-1, nums, diff)