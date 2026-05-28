class MyHashSet:

    def __init__(self):
        self.hashmap = []

    def add(self, key: int) -> None:
        self.hashmap.append(key)

    def remove(self, key: int) -> None:
        self.hashmap = [val for val in self.hashmap if val != key]
                
    def contains(self, key: int) -> bool:
        if key in self.hashmap:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)