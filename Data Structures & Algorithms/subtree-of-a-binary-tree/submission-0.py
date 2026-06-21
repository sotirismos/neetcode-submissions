# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, first_root, second_root):
        if not first_root and not second_root:
            return True
        if not first_root or not second_root:
            return False
        if first_root.val != second_root.val:
            return False
        return self.sameTree(first_root.left, second_root.left) and self.sameTree(first_root.right, second_root.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.sameTree(root, subRoot) | self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)