class Solution(object):
     def nextGreaterElement(self, nums1, nums2):
            ans = []
            mon_stk = []
       
            
            counter = defaultdict(int)
            for i in range(len(nums2)):
                if len(mon_stk)== 0:
                    mon_stk.append(nums2[i])
                elif  mon_stk[-1] > nums2[i]:
                    mon_stk.append(nums2[i])
                else:
                    while mon_stk and mon_stk[-1] < nums2[i]:
                        counter[mon_stk[-1]] = nums2[i] 
                        mon_stk .pop()
                        
                    mon_stk.append(nums2[i])
            for i in  mon_stk:
                counter[i] = -1
            
            for i in range(len(nums1)):
                
                ans.append(counter[nums1[i]])
            
            
            return ans
       
        