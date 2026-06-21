# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        first_queue = deque([p])
        second_queue = deque([q])
        
        while first_queue and second_queue:
            first_queue_level_lenght = len(first_queue)
            second_queue_level_lenght = len(second_queue)
            if first_queue_level_lenght != second_queue_level_lenght:
                return False
            for _ in range(first_queue_level_lenght):
                p_node = first_queue.popleft()
                q_node = second_queue.popleft()
                
                if not p_node and not q_node:
                    continue

                if not p_node or not q_node or p_node.val != q_node.val:
                    return False

                first_queue.append(p_node.left)
                first_queue.append(p_node.right)
                second_queue.append(q_node.left)
                second_queue.append(q_node.right)

        return True