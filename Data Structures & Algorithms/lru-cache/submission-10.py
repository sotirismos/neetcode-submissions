class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int: 
        if key in self.cache:
            self._remove_node(key)
            self._add_to_end(key, self.cache[key].val)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._remove_node(key)
            self._add_to_end(key, value)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_from_front()
            self._add_to_end(key, value)

    def _add_to_end(self, key: int, value: int) -> None:
        self.cache[key] = Node(key, value)
        previous = self.tail.prev
        previous.next = self.cache[key]
        self.cache[key].prev = previous
        self.cache[key].next = self.tail
        self.tail.prev = self.cache[key]

    def _remove_from_front(self) -> None:
        # Empty list not in our scope
        lru_node = self.head.next
        next_ = self.cache[lru_node.key].next
        self.head.next = next_
        next_.prev = self.head
        del self.cache[lru_node.key]
    
    def _remove_node(self, key: int) -> None:
       previous = self.cache[key].prev
       next_ = self.cache[key].next

       previous.next = next_
       next_.prev = previous













