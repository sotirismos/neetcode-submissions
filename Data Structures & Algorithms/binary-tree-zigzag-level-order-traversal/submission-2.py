# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque([root])
        zigzag_traversal = []

        level = 1
        while queue:
            current_level = []
            level_length = len(queue)

            for index in range(level_length):
                curr = queue.popleft()
                current_level.append(curr.val)

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            
            if (level % 2) != 0:
                zigzag_traversal.append(current_level[::-1])
            else:
                zigzag_traversal.append(current_level)

            level += 1
    
        return zigzag_traversal