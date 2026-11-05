# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            level_items = len(queue)
            # Retrieve first element from queue
            curr = queue.popleft()
            res.append(curr.val)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)

            # Pop remaining elemnents and add its children
            for counter in range(level_items - 1):
                curr = queue.popleft() 
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        
        return res
