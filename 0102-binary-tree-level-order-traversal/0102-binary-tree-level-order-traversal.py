# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = collections.defaultdict(list)
        q = collections.deque()
        q.append([root,0])
        while q:
            node,l = q.popleft()
            if node:
                levels[l].append(node.val)
                if node.left: q.append([node.left, l+1])
                if node.right: q.append([node.right, l+1])

        return list(levels.values())
        