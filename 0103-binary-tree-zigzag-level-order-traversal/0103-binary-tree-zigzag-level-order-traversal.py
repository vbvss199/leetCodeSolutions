# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this one sounds as a level order traversal using deque from collections may be lets give a try !!!!!!!
        queue=deque()
        if root is None:
            return []
        queue.append(root)
        levels=[]
        left_to_right=True
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            levels.append(level)
            left_to_right=not left_to_right
        return levels

