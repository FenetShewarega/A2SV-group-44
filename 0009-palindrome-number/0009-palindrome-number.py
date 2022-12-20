class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str= str(x)
        lis=[]
      
        reversedd=num_str[::-1]

        if reversedd == num_str :
            return True
        else:
            return False    