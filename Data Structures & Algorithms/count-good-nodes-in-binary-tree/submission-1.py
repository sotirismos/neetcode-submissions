# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque()

        if not root:
            return res

        queue.append((root, -float('inf')))
        while queue:
            node, max_val = queue.popleft()

            if node.val >= max_val:
                res += 1
            
            if node.left:
                queue.append((node.left, max(node.val, max_val)))
            
            if node.right:
                queue.append((node.right, max(node.val, max_val)))
        
        return res
        
        