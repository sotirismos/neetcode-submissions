# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid_subtree(node: TreeNode, low: int, high: int) -> bool:
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
                
            return is_valid_subtree(node.left, low, min(node.val, high)) and is_valid_subtree(node.right, max(node.val, low), high)  
                

        return is_valid_subtree(root, float('-inf'), float('inf'))

            
