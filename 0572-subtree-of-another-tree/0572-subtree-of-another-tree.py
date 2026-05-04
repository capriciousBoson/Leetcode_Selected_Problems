# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sameTree(self, node1,  node2):
        if node1 is None and node2 is None:
            return True
        elif node1 == None and node2 !=None:
            return False
        elif node1 != None and node2 == None:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = collections.deque()
        q.append(root)

        start_node = None
        while q:
            node = q.popleft()
            if node.val==subRoot.val:
                if self.sameTree(subRoot, node):
                    return True
            if node.left:
                if node.left.val==subRoot.left:
                    if self.sameTree(subRoot, node.left):
                        return True
                q.append(node.left)
            if node.right:
                if node.right.val==subRoot.val:
                    if self.sameTree(subRoot, node.right):
                        return True
                q.append(node.right)     

        
        return False
            