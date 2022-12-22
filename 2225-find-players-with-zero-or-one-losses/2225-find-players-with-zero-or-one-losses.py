class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        returned=[]
        lis1=[]
        lis2=[]
        counter1=defaultdict(int)
        counter2=defaultdict(int)
        
        for i in matches:
            counter1[i[0]]+=1
            
        for i in matches:
            counter2[i[1]]+=1
            
            
        for i in counter1:
            if i not in counter2:
                lis1.append(i)
                
        for j in counter2:
            if counter2[j]== 1:
                lis2.append(j)
                
        lis1.sort()
        lis2.sort()
        returned.append(lis1)
        returned.append(lis2)
        return(returned)
                
            

        