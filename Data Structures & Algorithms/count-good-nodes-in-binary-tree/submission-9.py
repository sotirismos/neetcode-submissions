# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_path_value):
            if not root:
                return 0

            # Recursion
            if root.val >= max_path_value:
                count = 1
                max_path_value = root.val
            else:
                count = 0
            
            left = dfs(root.left, max_path_value)
            right = dfs(root.right, max_path_value)

            # good nodes on current subtree
            curr_subtree = count + left + right

            return curr_subtree

        return dfs(root, float('-inf'))

