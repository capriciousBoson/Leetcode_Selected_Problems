# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            path = 1 + left_path + right_path

            max_path = max(max_path, path)
            return 1 + max(left_path, right_path)
        dfs(root)

        return max_path - 1
        