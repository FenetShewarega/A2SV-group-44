class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right
        queue = deque()
        visited = [[False]*n for _ in range(m)]
        steps = 0
        queue.append(entrance)
        visited[entrance[0]][entrance[1]] = True
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                curr = queue.popleft()
                
                if (curr[0] == 0 or curr[0] == m - 1 or curr[1] == 0 or curr[1] == n - 1) and curr != entrance:
                    return steps
                
                for dir in dirs:
                    r, c = curr[0] + dir[0], curr[1] + dir[1]
                    
                    if r < 0 or r >= m or c < 0 or c >= n or maze[r][c] == '+' or visited[r][c]:
                        continue
                    
                    queue.append([r, c])
                    visited[r][c] = True
            
            steps += 1
        
        return -1