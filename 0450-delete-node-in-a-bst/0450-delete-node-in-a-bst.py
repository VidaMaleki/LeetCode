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
        print("root is >>>" , root)
        print("left root is >>>", root.left)
        print("right root is >>>", root.right)
        if key < root.val:
            print("key < root")
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            print("key > root")
            root.right = self.deleteNode(root.right, key)
            
        else:  # Found the node to delete
            print("key == root")
            if not root.left:  # Case 2: One child (right)
                root = root.right
            elif not root.right:  # Case 2: One child (left)
                root = root.left
            else:  # Case 3: Two children
                successor = self.findSuccessor(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        print(root)
        return root


    def findSuccessor(self,node):
        print("successor start",node, node.left)
        while node.left:
            node = node.left
        print("successor end", node)
        return node






