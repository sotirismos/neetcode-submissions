# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, root, sub_root) -> bool:
        if not root and not sub_root:
            return True

        if (root and not sub_root) or (sub_root and not root):
            return False

        if root.val != sub_root.val:
            return  False

        left = self.isSametree(root.left, sub_root.left)
        right = self.isSametree(root.right, sub_root.right)
        
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSametree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right



