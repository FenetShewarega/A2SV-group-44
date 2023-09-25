class Solution(object):
    def bestTeamScore(self, scores, ages):
        
        store = []
        for i in range(len(scores)):
            store.append([scores[i] , ages[i]])
        store.sort()
        
        dp = [store[i][0] for i in range(len(scores))]
        for i in range(len(scores)):
            for j in range(i-1,-1, -1):
                if store[j][1] <= store[i][1]:
                    
                    dp[i] = max(dp[i] , store[i][0] + dp[j])
        return max(dp)
        
    
   