# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # CASE 1
        if not q and not p:
            return True
        # CASE 2.1
        if p and not q:
            return False
        if q and not p:
            return False
        # CASE 2.2          
        if not q and not p:
            return True
        # CASE 3
        if q and p:
            if q.val != p.val:
                return False
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

        return left and right        

