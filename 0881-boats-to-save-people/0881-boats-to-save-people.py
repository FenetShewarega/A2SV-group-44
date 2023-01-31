class Solution(object):
    def numRescueBoats(self, people, limit):
        # bo=[3,1,2,2]
        
        people.sort()
        i =  0
        ans = 0
        
        for j in range(len(people)-1,-1,-1):
            if i <= j:
                ans += 1
                if   people[i] + people[j] <= limit:
                    i += 1
                j -= 1
        return ans
        
        