class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total1=0
        total2=0
        
        for i in range(len(num1)):
            total1+=((ord(num1[i]))- 48 )*(10**((len(num1)-1)-i))
        
        for i in range(len(num2)):
            total2+=((ord(num2[i]))- 48 )*10**(len(num2)-1-i)
            
        return str(total2  * total1)                 
              