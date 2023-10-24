class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        strs = str(num)
        lists = list(strs)
        # print(lists)
        
        if len(set(lists) ) == 1 and lists[0] == '9':
            pass
        else:
            
            for i in range(len(lists)):
                if lists[i] != '9':
                    val = lists[i]
                    break

            for  i in range(len(lists)):
                if lists[i] == val:
                    lists[i] = '9'

            print(lists)
       
        strs2 = str(num)
        lists2 = list(strs2)
        val2 = lists2[0]
        print(val2)
        for i in range(len(lists2)):
            if lists2[i] == val2:
                lists2[i] = '0'

        max_res = "".join(lists)
        min_res = "".join(lists2)
        return int(max_res) - int(min_res)
