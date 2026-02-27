# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        # """
        # Do not return anything, modify root in-place instead.
        # """
        # # left pointer is always null and right should point to the next!
        # if root is None:
        #     return
        # self.flatten(root.right)
        # self.flatten(root.left)
        # root.right=self.prev
        # root.left=None
        # self.prev=root
        
        
        # lets go with the second approach stack
        if root is None:
            return []
        else:
            stack=[]
            stack.append(root)
            while(stack):
                current=stack.pop()
                if(current.right):
                    stack.append(current.right)
                if(current.left):
                    stack.append(current.left)
                if(stack):
                    current.right=stack[-1]
                current.left=None
    