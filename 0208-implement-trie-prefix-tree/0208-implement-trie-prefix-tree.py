class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        cur = self.root
    
        for i in range(len(word)):
            idx = ord(word[i])- 97
          
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True
        return 
    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i])- 97
            if  cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        if cur.isEnd:
            return True
        
        

    def startsWith(self, prefix):
        cur = self.root
       
        for i in range(len(prefix)):
            idx = ord(prefix[i])- 97

            if  cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return True
        
class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children =[ None for i in range(26)]

    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)