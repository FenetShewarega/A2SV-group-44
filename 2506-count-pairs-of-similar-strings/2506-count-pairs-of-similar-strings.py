class Solution(object):
    def similarPairs(self, words):
        counter = defaultdict(int)
        result=0
        for w in words:
            key = ' '.join(sorted(set(w)))
            result+= counter[key]
            counter[key] += 1
            
        return  result