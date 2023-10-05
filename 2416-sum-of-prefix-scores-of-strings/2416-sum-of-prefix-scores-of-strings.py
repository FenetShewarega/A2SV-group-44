class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        answer = []
        
        for word in words:
            trie.insert(word)
        
        for word in words:
            answer.append(trie.getPrefixScore(word))
        
        return answer

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.count += 1
    
    def getPrefixScore(self, word: str) -> int:
        current = self.root
        count = 0
        for char in word:
            if char in current.children:
                current = current.children[char]
                count += current.count
            else:
                break
        return count