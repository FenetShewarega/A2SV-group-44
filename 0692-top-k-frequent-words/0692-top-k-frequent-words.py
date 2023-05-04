class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = ["" for i in range(k)]
        sol=[]
        store = defaultdict(int)
        for i in range(len(words)):
            store[words[i]]+=1
            # print(store[i])
        store_ = sorted(store.items(),key =  lambda x:x[0] )
        # print(store_)
        store = dict(store_)
        result = sorted(store.items(),key =  lambda x:x[1] ,reverse = True)
        ans = sorted(result , key = lambda x :x[1] ,reverse = True )
        # print(ans)
        # print(result)
        for i in range(k):
            sol.append(result[i][0])
      
        return(sol)