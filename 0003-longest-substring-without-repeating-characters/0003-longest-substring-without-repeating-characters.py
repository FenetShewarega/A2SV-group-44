class Solution:
    def lengthOfLongestSubstring(self, s):
        substring =defaultdict(int)
        max_longest=0
        left=0
        right = 0
        while right < len(s):
             
            if s[right] not in substring:
                substring[s[right]] += 1
                max_longest = max(max_longest , right - left + 1)
                right+=1
            else:
                del substring[s[left]]
                left+=1
                 
        return max_longest       
                
                
       
           
            
       