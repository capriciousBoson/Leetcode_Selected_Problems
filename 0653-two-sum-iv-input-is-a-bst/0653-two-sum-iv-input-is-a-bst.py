# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        store = set()
        current = root
        def traverse(node):
            nonlocal store
            # print(f"store : {store}, node : {node}")
            if not node:
                return False
            diff =  k - node.val
            if diff in store:
                return True
            else:
                store.add(node.val)

                return traverse(node.left) or traverse(node.right)



        return traverse(current)




        