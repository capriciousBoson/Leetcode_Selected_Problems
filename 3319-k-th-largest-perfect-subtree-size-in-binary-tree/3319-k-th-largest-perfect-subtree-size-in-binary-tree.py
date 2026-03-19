# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def dfs(node):
            if not node:
                return 0, True

           
            ls, l_perfect = dfs(node.left) 
            rs, r_perfect = dfs(node.right)

            if ls==rs and l_perfect==r_perfect==True:
                res.append(1 + 2*ls)
                return 1 + 2*ls, True
            else:
                return 1 + ls + rs, False
        dfs(root)
        res.sort()
        return res[-k] if len(res) >= k else -1 
           
        