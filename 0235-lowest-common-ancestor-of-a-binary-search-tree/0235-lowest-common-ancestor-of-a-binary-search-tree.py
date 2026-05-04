# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None

            if node==p or node ==q:
                return node
            l = dfs(node.left)
            r = dfs(node.right)

            if l!=None and r != None:
                return node
            if l is None and r is None:
                return None
            if l is not None:
                return l
            if r is not None:
                return r
        return dfs(root)
            

        