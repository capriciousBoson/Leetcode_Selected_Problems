# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

 
        levels = collections.defaultdict(list)

        def dfs(l,i, node):
            if not node:
                return 

            levels[l].append(i)
            dfs(l+1, 2*i+1, node.left)
            dfs(l+1, 2*i+2, node.right)
        
        dfs(0,0, root)
        res = 0
        for level, idx in levels.items():
            res = max(res, idx[-1]-idx[0]+1)
        
        return res

        