# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        if q and not p:
            return False
        if not q and not p:
            return True

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p or queue_q:
            if len(queue_p) != len(queue_q):
                return False

            for level_nodes in range(len(queue_p)):
                curr_p = queue_p.popleft()
                curr_q = queue_q.popleft()
                
                if curr_p.val != curr_q.val:
                    return False

                if curr_q.left and curr_p.left:
                    queue_q.append(curr_q.left)
                    queue_p.append(curr_p.left)
                elif curr_q.left or curr_p.left:
                    return False
                
                if curr_q.right and curr_p.right:
                    queue_q.append(curr_q.right)
                    queue_p.append(curr_p.right)
                elif curr_q.right or curr_p.right:
                    return False
        return True
