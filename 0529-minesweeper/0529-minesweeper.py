class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal(i, j):
            if board[i][j] == 'E':
                count = 0
                for x, y in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]:
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                        count += 1
                if count == 0:
                    board[i][j] = 'B'
                    for x, y in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]:
                        if 0 <= x < m and 0 <= y < n:
                            reveal(x, y)
                else:
                    board[i][j] = str(count)
        
        m, n = len(board), len(board[0])
        
        i, j = click
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        reveal(i, j)
        
        return board