class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        result = []
        adj = [[] for _ in range(numCourses)]
        boolean = [[False] * numCourses for _ in range(numCourses)]

        for x in prerequisites:
            adj[x[0]].append(x[1])

        for i in range(numCourses):
            pq = deque()
            pq.append(i)
            seen = set()
            while pq:
                x = pq.popleft()
                if x in seen:
                    continue
                boolean[i][x] = True
                seen.add(x)

                for u in adj[x]:
                    pq.append(u)

        for x in queries:
            if boolean[x[0]][x[1]]:
                result.append(True)
            else:
                result.append(False)

        return result