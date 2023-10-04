class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        store = defaultdict(list)
        for i in range(len(times)):
            store[times[i][0]].append((times[i][1] ,times[i][2]))
        heap = [(0 , k)]
        visited = set()
        arr =[float(inf) for i in range(n+1)]
        arr[k]=0
        while heap:
            
            (cost , node) = heappop(heap)
            if node not in visited:
                visited.add(node)
            for n in store[node]:
                arr[n[0]] = min( cost + n[1] , arr[n[0]])
                if n[0] not in visited:
                    heappush(heap,(cost + n[1] , n[0] ))
            
        ans = max(arr[1:])
        
        return -1 if ans == inf else ans
                
            
            
            
    