class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot= 0
        for i in range(len(costs)):
            costs[i].append(abs(costs[i][0] - costs[i][1]))
        costs = sorted(costs , key = lambda x : x[2])  
        costs.reverse()
        print(costs)
        a = 0
        b = 0
        for i in range(len(costs)):
            
            if costs[i][0] > costs[i][1] :
                if b < len(costs) // 2:
                    tot +=  costs[i][1]
                    b+= 1
                else:
                    tot += costs[i][0]
            else  :
                if a < len(costs) // 2:
                        a += 1
                        tot += costs[i][0]
                else:
                      tot += costs[i][1]
        return tot
            
            
        
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     class Solution:

#     def swimInWater(self, grid: List[List[int]]) -> int:
#         # Dijkstra's Algorithm
#         n, m = len(grid), len(grid[0])
#         inbound = lambda r, c: 0 <= r < n and 0 <= c < m

#         min_time = defaultdict(lambda: float('inf'))
#         min_time[(0, 0)] = grid[0][0]
#         heap = [(grid[0][0], 0, 0)]
#         visited = set()
#         while heap:
#             time_, row, col = heappop(heap)
#             if (row, col) in visited:
#                 continue
#             visited.add((row, col))
#             for n_r, n_c in [(0, 1), (0, -1), (1, 0),  (-1, 0)]:
#                 next_cell = (row+n_r, col+n_c)
#                 if not inbound(next_cell[0], next_cell[1]):
#                     continue

#                 new_time = time_ + max(0, grid[next_cell[0]][next_cell[1]] - time_)
#                 if new_time < min_time[next_cell]:
#                     min_time[next_cell] = new_time
#                     heappush(heap, (new_time, next_cell[0], next_cell[1]))

#         return min_time[(n-1, m-1)]
        
# #         heap = [ ( costs[0][0] ,costs[0][1] )]
# #         visited = set()
        
# #         while heap:
            
        
        
        
        
     
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     