# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self,root,min,max):
        if root is None:
            return True
        # check where may be the code fails and capture it fail so that it fails we return false
        # if we check where the code is true it may be the first true but deep subtree there may be a false !
        if(root.val>=max or root.val<=min):
            return False
        return self.validate(root.left,min,root.val) and self.validate(root.right,root.val,max)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for every tree and sub tree we should left<node<right ! 
        return self.validate(root,float("-inf"),float("inf"))