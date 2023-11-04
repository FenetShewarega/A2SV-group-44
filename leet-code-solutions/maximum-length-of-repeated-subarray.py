class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
      
        max_subarray=''
        nums2_=''.join([chr(x) for x in nums2])
        print(nums2_)
        mx=0
        for num in nums1:
            max_subarray+= chr(num)
            print(chr(num))
            if max_subarray not in nums2_:
                   max_subarray = max_subarray[1:]
            else:
                mx=max(mx ,len(max_subarray))
        return mx  
      
         
