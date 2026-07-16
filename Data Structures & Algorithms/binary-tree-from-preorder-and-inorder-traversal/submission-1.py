# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash_map = {}
        for index, num in enumerate(inorder):
            inorder_hash_map[num] = index

        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])

        inorder_root_index = inorder_hash_map[root.val]

        iorder_left_subtree = inorder[:inorder_root_index]
        preorder_left_subtree = preorder[1: 1 + len(iorder_left_subtree)]

        inorder_right_subtree = inorder[inorder_root_index + 1:]
        preorder_right_subtree = preorder[1 + len(iorder_left_subtree):]

        root.left = self.buildTree(preorder_left_subtree, iorder_left_subtree)
        root.right = self.buildTree(preorder_right_subtree, inorder_right_subtree)

        return root        