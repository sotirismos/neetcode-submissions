# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, low, high = queue.popleft()
            if not low < node.val < high:
                return False
            
            if node.left:
                queue.append((node.left, low, min(node.val, high)))
            
            if node.right:
                queue.append((node.right, max(node.val, low), high))
                

        return True

            
