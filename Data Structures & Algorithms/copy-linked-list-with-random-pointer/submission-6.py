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
        mirrored_nodes = {}
        curr = head
        while curr:
            mirrored_nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        if curr:
            copy_head = mirrored_nodes[curr]
        else:
            copy_head = None
        
        copy_curr = copy_head
        while curr:
            if curr.next:
                copy_curr.next = mirrored_nodes[curr.next]
            else:
                copy_curr.next = None
            
            if curr.random:
                copy_curr.random = mirrored_nodes[curr.random]
            else:
                copy_curr.random = None

            copy_curr = copy_curr.next
            curr = curr.next
        
        return copy_head


        