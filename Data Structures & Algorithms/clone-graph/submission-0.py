"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node: Optional['node']) -> Optional['Node']:
            # Base case
            if node in old_to_new:
                return old_to_new[node]
 
            # Clone (choose)
            clone = Node(node.val)
            old_to_new[node] = clone

            # Explore
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                clone.neighbors.append(cloned_neighbor)
            
            return clone
        
        if node:
            return dfs(node)
        else:
            None