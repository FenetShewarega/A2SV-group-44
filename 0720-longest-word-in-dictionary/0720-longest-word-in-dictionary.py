class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        for word in words:
            self.insert(word)
        sol = [] 
        x = []
        dic = defaultdict(list)
        for i in range(len(words)):
            x.append([len(words[i]), words[i]])
        x.sort(reverse=True)

        for i in range(len(x)):
            word = x[i][1]
            count = 0
            for j in range(len(word)):
                if self.search(word[:j]):
                    count += 1
            if count == len(word) - 1:
                sol.append(word)
    
        for i in sol:
            dic[len(i)].append(i)
        for i in dic:
            dic[i].sort()
            n = dic[i]
            
            return n[0]
        return ''

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.isEnd

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26