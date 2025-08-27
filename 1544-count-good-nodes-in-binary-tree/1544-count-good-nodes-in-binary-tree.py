# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, prevmax):
            nonlocal count

            if not node: return

            if prevmax <= node.val:
                count += 1
            prevmax = max(prevmax, node.val)
            
            dfs(node.left, prevmax)
            dfs(node.right, prevmax)
            return
        dfs(root, -float('inf'))
        return count
        