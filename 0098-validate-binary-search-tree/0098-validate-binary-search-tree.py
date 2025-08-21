# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, l, r):
            if not node:
                return True
            if node.val <=l or node.val >= r:
                return False
            
            return validate(node.left, l, node.val) and validate(node.right, node.val, r)
        return validate(root, -float('inf'), float('inf'))