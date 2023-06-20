class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([('0000', 0)])
        visited = set(['0000'])
        while queue:
            
            position, moves = queue.popleft()
            if position == target:
                return moves
            if position in deadends:
                continue
            for i in range(4):
                for d in (-1, 1):
                    new_pos = position[:i] + str((int(position[i]) + d) % 10) + position[i+1:]
                    if new_pos not in visited:
                        visited.add(new_pos)
                        queue.append((new_pos, moves+1))
        return -1