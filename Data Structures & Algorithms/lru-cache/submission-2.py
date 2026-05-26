class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            key_to_be_removed = self.lru[0]
            self.lru.pop(0)
            del self.cache[key_to_be_removed]
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        else:
            self.lru.append(key)
        self.cache[key] = value
        