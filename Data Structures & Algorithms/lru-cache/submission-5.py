class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}                 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head           

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        self.move_to_front(self.key_to_node[key])
        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.move_to_front(self.key_to_node[key])
        else: 
            if len(self.key_to_node) < self.capacity:
                self.key_to_node[key] = Node(key, value)
                self.add_to_front(self.key_to_node[key])
            else:
                node_to_be_removed = self.tail.prev
                self.remove(node_to_be_removed)
                del self.key_to_node[node_to_be_removed.key]
                self.key_to_node[key] = Node(key, value)
                self.add_to_front(self.key_to_node[key])           
    
    def remove(self, node) -> None:
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node 

    def add_to_front(self, node) -> None:
        first_node = self.head.next
        node.prev = self.head
        node.next = first_node
        self.head.next = node
        first_node.prev = node

    def move_to_front(self, node) -> None:
        self.remove(node)
        self.add_to_front(node)
