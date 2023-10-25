class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        answer = []

        for query in queries:
            center_x, center_y, radius = query
            count = 0

            for point in points:
                point_x, point_y = point
                distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
                if distance <= radius:
                    count += 1

            answer.append(count)

        return answer