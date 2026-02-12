# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # lets use the level order traversal and reurn the length of the levels array
        levels=[]
        if root is None:
            return len(levels)
        else:
            queue=deque()
            queue.append(root)
            while(queue):
                level=[]
                for _ in range(len(queue)):
                    node=queue.popleft()
                    level.append(node.val)
                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
                levels.append(level)
        return len(levels)