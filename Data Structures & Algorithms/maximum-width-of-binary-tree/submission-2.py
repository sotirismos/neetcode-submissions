# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 0])
        max_width = 0

        # How will I define that a node was added in order to start counting?
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                curr, level_index = queue.popleft()

                # Retrieve first element from current level
                if i == 0:
                    starting_index = level_index
                # Retrive last element from current level
                if i == (level_length - 1):
                    last_index = level_index

                if curr.left:
                    queue.append([curr.left, level_index * 2])
                
                if curr.right:
                    queue.append([curr.right, level_index * 2 + 1])
            
            max_width = max(max_width, last_index - starting_index + 1)
        
        return max_width
            

