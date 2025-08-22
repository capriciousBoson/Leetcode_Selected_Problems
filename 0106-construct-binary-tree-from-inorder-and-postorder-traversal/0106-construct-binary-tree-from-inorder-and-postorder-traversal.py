# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_index = {inorder[i]:i for i in range(n)}

        post_idx = n-1
        def build(inorder_start, inorder_end):
            nonlocal post_idx
            if inorder_start > inorder_end:
                return 
            
            root = TreeNode(postorder[post_idx])
            root_idx = inorder_index[postorder[post_idx]]
            post_idx -= 1
            root.right = build(root_idx+1, inorder_end)

            root.left = build(inorder_start, root_idx-1)
            return root
        tree_root = build(0, n-1)
        return tree_root