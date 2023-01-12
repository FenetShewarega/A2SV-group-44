class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        count=defaultdict(int)
        # out_put = [Counter(i) for i in words]
        out_put = []
        ans = []
        
        for i in range(len(words)) :
            new_count = defaultdict(int)
            for j in range(len(words[i])):
                new_count[words[i][j]] += 1     
            out_put.append(new_count)   
            
        for i in out_put[0]:
            min_ = 101
            cnt = 0
            for j in range(len(out_put)):
                if i in out_put[j]:
                    min_ =  min(out_put[j][i],min_)
                    cnt+=1
            if cnt == len(words) :
                ans += [i] * min_
                
            
            
        return(ans)         
                
                
                
        # for x in count:
        #     if count[x] == len(words):
        #         out_put.append(x)
        # print(out_put) 
        # return out_put        