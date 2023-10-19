class Solution:
    def countPrimes(self, n: int) -> int:
        if n ==0 or n ==1:
            return 0
        
        
        s = [True for _ in range( n )]
        p = 2
        while (p * p  <= n):
            if s[p]== True:
                for i in range(p * p , n , p):
                    s[i] = False
            p+=1
        # print(s)
        count = 0
        for i in s:
            if i:
                count += 1
       
        return  count - 2