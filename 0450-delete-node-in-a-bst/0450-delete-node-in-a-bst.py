# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteHelper(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        current = node.left
        while current.right:
            current = current.right
        
        current.right = node.right

        return node.left


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : return root

        print(f"root : {root}")
        if root.val == key:
            print("deleteing thr root node-----")
            return self.deleteHelper(root)
        current = root
        

        while current:
            if current.val > key:
                if current.left:
                    if current.left.val==key:
                        current.left = self.deleteHelper(current.left)
                        break
                    else:
                        current = current.left
                else:
                    break
                
            elif current.val < key:
                if current.right:
                    if current.right.val==key:
                        current.right = self.deleteHelper(current.right)
                        break
                    else:
                        current = current.right
                else:
                    break
        
        
        return root

                    
                




        