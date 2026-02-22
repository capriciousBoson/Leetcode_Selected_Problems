# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balance = True
        
        def height(node):
            nonlocal balance
            if not node:
                return 0
            
            l = height(node.left)
            r = height(node.right)
            # print(f"for node: {node.val} | left : {l} , right : {r}")
            if abs(l-r) > 1:
                balance  = False
            return 1 + max(l,r)
        height(root)
        return balance
