# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_subtree_height = self.maxHeight(root.left)
        right_subtree_height = self.maxHeight(root.right)
        
        max_height = max(1 + left_subtree_height, 1 + right_subtree_height)

        return max_height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter = self.maxHeight(root.left) + self.maxHeight(root.right)
        max_subtree_diameter = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        return max(diameter, max_subtree_diameter)