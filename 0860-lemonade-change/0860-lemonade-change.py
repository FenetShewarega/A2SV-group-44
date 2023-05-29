class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        tot = 0
        for i in range (len(bills)):
            if bills[i] == 5:
                total += 1
            elif bills[i] == 10:
                if total == 0:
                    return False
                total -= 1
                tot += 1
            else:
                if tot and total:
                    tot -= 1
                    total -= 1
                elif total >= 3:
                    total -= 3
                else:
                    return False
        return True
            