# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            l = search(node.left)
            r = search(node.right)
            if l and r :
                return node
            return l if l else r
        return search(root)
            

        