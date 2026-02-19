# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderTraversal(self,root:Optional[TreeNode])->int:
        if root is None:
            return []
        queue=deque()
        queue.append((root,0))
        while(queue):
            min_index = min(index for node, index in queue)
            size=len(queue)
            for i in range(size):
                first_index=last_index=0
                node,index=queue.popleft()
                # normalisation to prevent the overflow !
                index=index-min_index
                
                if i==0:
                    first_index=index
                if i==size-1:
                    last_index=index

                if node.left:
                    queue.append((node.left,2*index+1))
                if node.right:
                    queue.append((node.right,2*index+2))
            self.maxWidth=max(self.maxWidth,last_index-first_index+1)
        return self.maxWidth

        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # add all the levels into the list and after adding return the one which has the maximum 
        # before that if we encounter the null in the level order traversal add that as well
        self.maxWidth=float("-inf")
        return self.levelOrderTraversal(root)
        # write a logic to pull out the maximum 