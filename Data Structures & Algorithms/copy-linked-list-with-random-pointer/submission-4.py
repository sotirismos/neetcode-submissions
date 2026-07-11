"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        curr = head
        while curr:
            nodes[curr] = Node(x = curr.val)
            curr = curr.next

        curr = head
        clone_head = nodes[curr]
        clone_curr = clone_head        
        while curr:
            clone_curr.next = nodes[curr.next] if curr.next else None
            clone_curr.random = nodes[curr.random] if curr.random else None
    
            curr = curr.next
            if curr:
                clone_curr = nodes[curr]
        return clone_head
