class Solution:
    def kWeakestRows(self ,matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])
        row_strengths = []

        for i in range(rows):
            count = 0
            for j in range(cols):
                if matrix[i][j] == 1:
                    count += 1
                else:
                    break
            row_strengths.append((count, i))

        row_strengths.sort()

        w = []
        for i in range(k):
            w.append(row_strengths[i][1])

        return w