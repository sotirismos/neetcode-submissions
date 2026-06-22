# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.count

        max_val = root.val

        def count_func(node: TreeNode, max_val: int):
            if not node:
                return 0

            if node.val >= max_val:
                self.count += 1
            
            node.left = count_func(node.left, max(max_val, node.val))
            node.right = count_func(node.right, max(max_val, node.val))

            return self.count
        
        return count_func(root, max_val)
        
        