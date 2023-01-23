class Solution(object):
    def pancakeSort(self, arr):
        
        move = []
        
        for k in range(len(arr),1,-1):
            index = arr.index(k)+1
            
            if index == k:
                continue
            if index != 1:
                move.append(index)
                arr = arr[:index][::-1] + arr[index:]
            move.append(k)
            arr = arr[:k][::-1] + arr[k:]
        return move
