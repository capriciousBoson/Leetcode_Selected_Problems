# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        current = root

        while current:
            if current.val >= val:
                if current.left is not None:
                    current = current.left
                    
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
        return root
            
        