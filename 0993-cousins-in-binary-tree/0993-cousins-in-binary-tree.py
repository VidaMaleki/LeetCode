from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None, 0)])
        x_info = None
        y_info = None
        while queue:
            current, parent, depth = queue.popleft()
            
            if current.val == x:
                x_info = (parent, depth)
                
            if current.val == y:
                y_info = (parent, depth)
            
            if x_info and y_info:
                break
            if current.left:
                queue.append((current.left, current, depth+1))
            if current.right:
                queue.append((current.right, current, depth+1))
        if x_info and y_info:
            return x_info[1] == y_info[1] and x_info[0] != y_info[0]
        return False

                

