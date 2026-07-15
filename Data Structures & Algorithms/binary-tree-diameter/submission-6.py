# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left_subtree_height = maxHeight(root.left)
            right_subtree_height = maxHeight(root.right)
            
            self.max_diameter = max(self.max_diameter, left_subtree_height +  right_subtree_height)

            max_height = max(1 + left_subtree_height, 1 + right_subtree_height)

            return max_height
        
        maxHeight(root)
        
        return self.max_diameter       