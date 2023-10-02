class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.value = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return self.search(cur)

    def search(self, cur: TrieNode) -> int:
        result = cur.value
        for child in cur.children.values():
            result += self.search(child)
        return result