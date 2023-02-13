class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        [4 ,7 ,9]
        [2 , 5 ,8 ,8]
        count = 0
        left  = len(players) - 1
        right = len(trainers) - 1
        trainers.sort()
        players.sort()
        while right >= 0 and left >= 0:
            if players[left] <= trainers[right]:
                count += 1
                right  -= 1
                left -= 1
            else: 
                left-=1
        return(count)        
                
                
                
                