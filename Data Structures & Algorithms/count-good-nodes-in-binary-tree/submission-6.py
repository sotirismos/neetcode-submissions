# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def count_dfs(root: TreeNode, max_value: int) -> int:
            total = 0
            if not root:
                return total

            if root.val >= max_value:
                total += 1

            max_value = max(max_value, root.val)

            if root.left:
                total += count_dfs(root.left, max_value)
            if root.right:
                total += count_dfs(root.right, max_value)

            return total
            
        left = count_dfs(root.left, root.val)
        right = count_dfs(root.right, root.val)

        return left + right + 1