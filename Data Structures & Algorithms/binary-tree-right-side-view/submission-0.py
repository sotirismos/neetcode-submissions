# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        if not root:
            return right_view

        queue = deque([root])
        while queue:
            level_lenght = len(queue)
            for count in range(level_lenght):
                node = queue.popleft()
                if count == 0:
                    right_view.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return right_view