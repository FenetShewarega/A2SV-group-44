class MyHashMap:

    def __init__(self):
        self.store = defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.store[key] = value

    def get(self, key: int) -> int:
        return self.store[key] if key in self.store  else -1

    def remove(self, key: int) -> None: 
        if key in self.store:
            del self.store[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)