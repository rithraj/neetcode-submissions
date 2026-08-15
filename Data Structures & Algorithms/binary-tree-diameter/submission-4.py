# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0                     # (height, diameter)

            l_h, l_d = dfs(node.left)          # left subtree info
            r_h, r_d = dfs(node.right)         # right subtree info

            height_here = 1 + max(l_h, r_h)    # include this node
            through_here = l_h + r_h           # path using both sides
            best_diam = max(l_d, r_d, through_here)

            return height_here, best_diam

        _ , d =  dfs(root)
        return d
        