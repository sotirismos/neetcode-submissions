# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            for _ in range(len(queue)):
                curr, min_val, max_val = queue.popleft()
                
                if min_val >= curr.val or curr.val >= max_val:
                    return False
                
                if curr.left:
                    queue.append((curr.left, min_val, curr.val))
                if curr.right:
                    queue.append((curr.right, curr.val, max_val))
        return True