from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        # Initialize distances with negative infinity
        distances = [float('-inf')] * n
        distances[start] = 1.0

        # Priority queue to store nodes and their probabilities
        pq = [(-1.0, start)]

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  

            if node == end:
                return prob

            if prob < distances[node]:
                continue 

            for neighbor, neighbor_prob in graph[node]:
                new_prob = prob * neighbor_prob

                if new_prob > distances[neighbor]:
                    distances[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0.0