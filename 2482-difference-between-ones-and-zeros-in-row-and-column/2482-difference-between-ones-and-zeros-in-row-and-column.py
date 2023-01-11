class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
       
        ROWS, COLS = len(grid), len(grid[0])
        
        row1sum = [0] * ROWS
        col1sum = [0] * COLS
        row0sum = [0] * ROWS
        col0sum = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                row1sum[r] += grid[r][c]
                col1sum[c] += grid[r][c]
                if grid[r][c] == 0:
                    row0sum[r] += 1
                    col0sum[c] += 1
        dif = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                dif[r][c] = row1sum[r]+col1sum[c]-row0sum[r]-col0sum[c]
        return dif