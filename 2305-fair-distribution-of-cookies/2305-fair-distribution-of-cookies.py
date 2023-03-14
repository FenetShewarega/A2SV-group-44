class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        self.cookies = cookies
        c= [0 for i in range(k)]
        return self.recurence(0 , c, k)
    def recurence( self , index , children, k ):
        if index >= len(self.cookies) :
            return max(children)
        minimum = inf
        for i in range(k):
            children[i] += self.cookies[index]
            if children[i] < minimum:
                curr  = self.recurence(index + 1 , children , k)
                minimum = min(minimum , curr)
            children[i] -= self.cookies [index]
        return minimum  