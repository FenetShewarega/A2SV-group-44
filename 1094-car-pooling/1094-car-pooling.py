class Solution:
    def carPooling(self, trip: List[List[int]], capacity: int) -> bool:
        rng=-1
        for _,_,end in trip:
            rng=max(rng,end)
        arr=[0] * (rng  +1  )
        # print(arr)
        for pas,start,end in trip:
            if end <= len(arr):
                arr[start] += pas
                arr[end] -= pas
        if   arr[0] > capacity :
            return False
        for i in range(1,len(arr)):
            arr[i]+= arr[i-1]
            if arr[i] > capacity:
                return False 
        return True
        
        
       
        #   0  1  2  3  4  5  6  7  8 
        # # 0 ,0 ,0 ,0, 0, 0, 0, 0  0
        # # 2  0   0  0  0 1  0  0 
        
        
        
