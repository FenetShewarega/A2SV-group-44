class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)

        tasks.sort()        
        flag = [0] * n
        start = 1
        i = 0
        pq = []
        ans = []

        while i < n:
            while i < n and tasks[i][0] <= start:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not pq:
                ans.append(tasks[i][2])
                start = tasks[i][0] + tasks[i][1]
                i += 1
            else:
                processing_time, index = heapq.heappop(pq)
                ans.append(index)
                start += processing_time

        while pq:
            processing_time, index = heapq.heappop(pq)
            ans.append(index)
            start += processing_time

        return ans