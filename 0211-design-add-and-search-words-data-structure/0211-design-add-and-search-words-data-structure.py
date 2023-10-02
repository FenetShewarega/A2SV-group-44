class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        return self.searchUtil(word, self.root)

    def searchUtil(self, word: str, node) -> bool:
        cur = node
        for i in range(len(word)):
            if word[i] == '.':
                for child in cur.children:
                    if child and self.searchUtil(word[i+1:], child):
                        return True
                return False

            idx = ord(word[i]) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]

        return cur.isEnd


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26