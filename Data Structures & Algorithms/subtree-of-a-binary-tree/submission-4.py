# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (subRoot and not root):
            return False
        if root and subRoot:
            if root.val != subRoot.val:
                return False
            left = self.isSameTree(root.left, subRoot.left)
            right = self.isSameTree(root.right, subRoot.right)
        
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return False
        
        is_sub = self.isSameTree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return is_sub or left or right
        