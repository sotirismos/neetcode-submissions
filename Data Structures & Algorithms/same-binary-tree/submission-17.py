# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        if (p and not q) or (q and not p):
            return False

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            for _ in range(len(queue_p)):
                curr_p = queue_p.popleft()
                curr_q = queue_q.popleft()
                
                if curr_p.val != curr_q.val:
                    return False
                
                if curr_p.left and curr_q.left:
                    queue_p.append(curr_p.left)
                    queue_q.append(curr_q.left)
                if curr_p.left and not curr_q.left or curr_q.left and not curr_p.left:
                    return False

                if curr_p.right and curr_q.right:
                    queue_p.append(curr_p.right)
                    queue_q.append(curr_q.right)
                if curr_p.right and not curr_q.right or curr_q.right and not curr_p.right:
                    return False
        
        if len(queue_p) != len(queue_q):
            return False
        else:
            return True
