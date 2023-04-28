class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([rooms[0]])
        visited = set([0])
        
        while queue:
            keys = queue.popleft()
           
            for i in range(len(keys)):
                
                if keys[i] not in visited:
                    visited.add(keys[i])
                    queue.append(rooms[keys[i]])
                
        for i in range(len(rooms)):
            if i not in visited:
                return False
                
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
            