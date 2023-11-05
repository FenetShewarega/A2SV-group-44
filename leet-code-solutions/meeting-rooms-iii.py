class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
            cnt = [0] * 101
            meetings.sort()
            pq = []
            for i in range(n):
                heapq.heappush(pq, (meetings[0][0], i))
            for m in meetings:
                while pq[0][0] < m[0]:
                    
                    
                    
                    start, room = heapq.heappop(pq)
                    heapq.heappush(pq, (m[0], room))
                start, room = heapq.heappop(pq)
                
                
                heapq.heappush(pq, (start + m[1] - m[0], room))
                cnt[room] += 1
            return cnt.index(max(cnt))