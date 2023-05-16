# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key) 
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) 
        else:  # Found the node to delete
            if not root.left:  # key has One child (right)
                root = root.right
            elif not root.right:  #Key has One child (left)
                root = root.left
            else:  # key has Two children and we need to choose right one
                successor = self.findSuccessor(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        return root


    def findSuccessor(self,node):
        # if right node has left node choose that otherwise replace with right
        while node.left:
            node = node.left
        return node






