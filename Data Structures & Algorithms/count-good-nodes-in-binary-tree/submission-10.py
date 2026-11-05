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
        
        counter = 0
        max_val = root.val
        queue = deque([(root, float('-inf'))])

        while queue:
            for _ in range(len(queue)):
                curr_node, max_val = queue.popleft()

                if curr_node.val >= max_val:
                    counter += 1
                    max_val = curr_node.val
                
                if curr_node.left:
                    queue.append((curr_node.left, max_val))
                if curr_node.right:
                    queue.append((curr_node.right, max_val))
        
        return counter


