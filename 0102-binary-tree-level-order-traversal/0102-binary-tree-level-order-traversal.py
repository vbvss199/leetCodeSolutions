# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use a queue to perform the bfs  
        queue=deque([root])
        #every time the level is appended as a list to the levels list
        levels=[]
        # write the logic here !!!
        if root is None:
            return levels
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)

        return levels
