class Solution:
        def numTeams(self, rating: List[int]) -> int:
            n = len(rating)

            up = [0] * n
            down = [0] * n

            count = 0

            for i in range(n):
                for j in range(i, -1, -1):
                    if rating[i] > rating[j]:
                        up[i] += 1
                        count += up[j]

            for i in range(n):
                for j in range(i, -1, -1):
                    if rating[i] < rating[j]:
                        down[i] += 1
                        count += down[j]

            return count