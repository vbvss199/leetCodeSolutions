# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # for each node in the level order traversal update the leftmost node as the one which goes first to the levels list using the deque from collections !!!!!!! 
        # lets give a fucking try to this 
        queue=deque()
        if root is None:
            return None
        queue.append(root)
        # to store the leftmost node val
        leftMostNodeVal=root.val
        while(queue):
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            # after everything is done re assign the last element of the level to the leftMostNodeVal
            leftMostNodeVal=level[0]
        return leftMostNodeVal