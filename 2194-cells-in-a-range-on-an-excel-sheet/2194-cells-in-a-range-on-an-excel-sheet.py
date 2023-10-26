class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cell1, cell2 = s.split(':')
        col1, row1 = cell1[:-1], int(cell1[-1:])
        col2, row2 = cell2[:-1], int(cell2[-1:])

        cells = []
        for row in range(row1, row2 + 1):
            for col_num in range(ord(col1), ord(col2) + 1):
                col = chr(col_num)
                cells.append(col + str(row))

        cells.sort()
        return cells