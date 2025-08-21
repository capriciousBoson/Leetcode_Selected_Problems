# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        current = root

        while current:
            if current.left is None:
                res.append(current.val)
                current = current.right
            else:
                # connect the last node of the left subtree to the current node
                lastnode = current.left
                while lastnode.right and lastnode.right != current:
                    lastnode = lastnode.right
                
                if lastnode.right is None:
                    lastnode.right = current
                    # now we can go in the left subtree
                    current = current.left
                
                elif lastnode.right == current:
                    # left subtree is already explored
                    lastnode.right = None
                    res.append(current.val)
                    current = current.right
        return res

        