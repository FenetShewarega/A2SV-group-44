class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        directions = [(-1, 1), (1, -1)]
        curr_direction = 0
        n, m = len(mat), len(mat[0])
        element_count = 0
        
        ans = []
        curr_row, curr_col = 0, 0
        in_bound = lambda x, y : 0 <= x < n and 0 <= y < m
        
        while element_count < n * m:
            dx, dy = directions[curr_direction]
            if in_bound(curr_row, curr_col):
                ans.append(mat[curr_row][curr_col])
                curr_row, curr_col = curr_row + dx, curr_col + dy
                element_count += 1
                
            else:
                if curr_col >= m:
                    curr_row, curr_col = curr_row - dx + 1, curr_col - dy
                elif curr_row >= n:
                    curr_row, curr_col = curr_row - dx, curr_col - dy + 1
                elif curr_row < 0:
                    curr_row, curr_col = curr_row - dx, curr_col - dy + 1
                elif curr_col < 0:
                    curr_row, curr_col = curr_row - dx + 1, curr_col - dy
                
                curr_direction = 1 - curr_direction
            
        return ans