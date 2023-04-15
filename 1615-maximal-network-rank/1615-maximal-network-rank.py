class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        r = defaultdict(list)
        for i in range(len(roads)):
            
            r[roads[i][0]].append(roads[i][1])
            r[roads[i][1]].append(roads[i][0])
            
        max_rank = 0
        
        for i in range(n):
            for j in range(i+1 , n):
                
                rank = len(r[i]) + len(r[j]) 
                
                if i in r[j]:
                    
                    rank -= 1
                max_rank=max(rank, max_rank)
                
        return max_rank
   
        