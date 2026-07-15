# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_subtree_height = self.maxHeight(root.left)
        right_subtree_height = self.maxHeight(root.right)

        max_height = max(1 + left_subtree_height, 1 + right_subtree_height)

        return max_height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.max_diameter
        
        self.max_diameter = max(self.max_diameter, self.maxHeight(root.left) + self.maxHeight(root.right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.max_diameter       