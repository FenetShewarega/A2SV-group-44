class Solution:
    def champagneTower(self ,poured: int, query_row: int, query_glass: int) -> float:
        pyramid = [[0 for _ in range(100)] for _ in range(100)]
        pyramid[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if pyramid[i][j] > 1:
                    overflow = (pyramid[i][j] - 1) / 2
                    if i+1 < 100:
                        pyramid[i+1][j] += overflow
                        pyramid[i+1][j+1] += overflow
                    pyramid[i][j] = 1
        return min(1, pyramid[query_row][query_glass])