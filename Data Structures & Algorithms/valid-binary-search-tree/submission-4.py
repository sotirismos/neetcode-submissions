# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        right = float("-inf")
        left = float("inf")

        def valid(node: TreeNode, right: int, left: int) -> bool:
            if not node:
                return True
            
            if not right < node.val < left:
                return False
            
            return valid(node.left, right, node.val) and valid(node.right, node.val, left)

        return valid(root, right, left)