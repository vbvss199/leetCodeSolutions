# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        if root is None:
            return []
        queue.append(root)
        # store the list of values here in a list 
        rightMostNodeVallist=[]
        while(queue):
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            # now need to assign the last element of the level
            rightMostNodeVallist.append(level[-1])
        return rightMostNodeVallist