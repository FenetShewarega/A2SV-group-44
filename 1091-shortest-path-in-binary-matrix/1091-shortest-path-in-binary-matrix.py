class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue = deque([(0,0)])
        dire_arr = [[0,1],[1,0],[1,1],[-1,-1],[-1,0],[0,-1],[-1,1],[1,-1]]
        vis = set()
        dist = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n-1 and y == n-1:
                    return dist
                for dx, dy in dire_arr:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0 and (new_x, new_y) not in vis:
                        vis.add((new_x, new_y))
                        queue.append((new_x, new_y))
            dist += 1
        return -1
        